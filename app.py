import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import filedialog, colorchooser, font as tkFont
from tkinter.messagebox import showerror, askyesno, showinfo
from PIL import Image, ImageOps, ImageTk, ImageFilter, ImageGrab
APP_NAME = "Multimedia project"
APP_THEME = "vapor"
CANVAS_BG_COLOR = "#2C3034"
PLACEHOLDER_TEXT_COLOR = "#A9A9A9"
LEFT_PANEL_WIDTH = 240
MAIN_CANVAS_WIDTH = 800
MAIN_CANVAS_HEIGHT = 600
IMAGE_DISPLAY_AREA_WIDTH = MAIN_CANVAS_WIDTH - 20
IMAGE_DISPLAY_AREA_HEIGHT = MAIN_CANVAS_HEIGHT - 20
file_path = ""
pen_size = 3
pen_color = "#FFFFFF"
is_flipped = False
rotation_angle = 0
current_pil_image_full_res = None
displayed_photo_image = None
status_bar_label = None
def update_status(message, clear_after_ms=0):
    if status_bar_label:
        status_bar_label.config(text=message)
        if clear_after_ms > 0:
            status_bar_label.after(clear_after_ms, lambda: status_bar_label.config(text="Ready"))
def _calculate_aspect_fit_dims(orig_w, orig_h, target_w, target_h):
    if orig_w == 0 or orig_h == 0: return 0, 0
    orig_aspect = orig_w / orig_h
    target_aspect = target_w / target_h
    if orig_aspect > target_aspect:
        new_w = target_w
        new_h = int(new_w / orig_aspect)
    else:
        new_h = target_h
        new_w = int(new_h * orig_aspect)
    return new_w, new_h
def _draw_canvas_placeholder():
    canvas.delete("all")
    placeholder_font = tkFont.Font(family="Helvetica", size=16, weight="bold")
    canvas.create_text(
        IMAGE_DISPLAY_AREA_WIDTH / 2,
        IMAGE_DISPLAY_AREA_HEIGHT / 2,
        text="Open an Image to Begin",
        font=placeholder_font,
        fill=PLACEHOLDER_TEXT_COLOR,
        anchor="center",
        tags="placeholder"
    )
    canvas.displayed_image_width = 0
    canvas.displayed_image_height = 0
def _update_canvas_image(pil_img_full_res_to_display):
    global current_pil_image_full_res, displayed_photo_image, canvas
    current_pil_image_full_res = pil_img_full_res_to_display
    canvas.delete("all")
    if current_pil_image_full_res is None:
        _draw_canvas_placeholder()
        return
    img_w, img_h = current_pil_image_full_res.size
    display_w, display_h = _calculate_aspect_fit_dims(
        img_w, img_h, IMAGE_DISPLAY_AREA_WIDTH, IMAGE_DISPLAY_AREA_HEIGHT
    )
    if display_w <= 0 or display_h <= 0:
        _draw_canvas_placeholder()
        return
    image_for_tk = current_pil_image_full_res.resize((display_w, display_h), Image.LANCZOS)
    displayed_photo_image = ImageTk.PhotoImage(image_for_tk)
    display_x = (IMAGE_DISPLAY_AREA_WIDTH - display_w) / 2
    display_y = (IMAGE_DISPLAY_AREA_HEIGHT - display_h) / 2
    canvas.create_image(display_x, display_y, anchor="nw", image=displayed_photo_image, tags="background_image")
    canvas.image = displayed_photo_image
    canvas.displayed_image_width = display_w
    canvas.displayed_image_height = display_h
    canvas.display_offset_x = display_x
    canvas.display_offset_y = display_y
def open_image_file():
    global file_path, is_flipped, rotation_angle
    update_status("Opening file dialog...")
    new_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.gif;*.bmp"), ("All Files", "*.*")]
    )
    if new_path:
        file_path = new_path
        is_flipped = False
        rotation_angle = 0
        update_status(f"Loading {file_path.split('/')[-1]}...")
        try:
            pil_img = Image.open(file_path)
            if pil_img.mode != 'RGBA': pil_img = pil_img.convert('RGBA')
            _update_canvas_image(pil_img)
            filter_combobox.current(0)
            update_status(f"Loaded: {file_path.split('/')[-1]}", 3000)
        except Exception as e:
            showerror("Error Opening Image", f"Could not open or read image file.\n{e}")
            file_path = ""
            _update_canvas_image(None)
            update_status("Failed to load image", 3000)
    else:
        update_status("Open cancelled", 2000)
    update_button_states()
def _get_current_transformed_pil_image():
    if not file_path: return None
    try:
        pil_img = Image.open(file_path)
        if pil_img.mode != 'RGBA': pil_img = pil_img.convert('RGBA')
        if is_flipped:
            pil_img = pil_img.transpose(Image.FLIP_LEFT_RIGHT)
        if rotation_angle != 0:
            pil_img = pil_img.rotate(rotation_angle, expand=True, fillcolor=(0,0,0,0))
        selected_filter = filter_combobox.get()
        if selected_filter != "Original":
            update_status(f"Applying {selected_filter} filter...")
            if selected_filter == "Black and White": pil_img = ImageOps.grayscale(pil_img.convert('RGB')).convert('RGBA')
            elif selected_filter == "Sepia":
                 sepia_matrix = [
                    0.393, 0.769, 0.189, 0,
                    0.349, 0.686, 0.168, 0,
                    0.272, 0.534, 0.131, 0]
                 pil_img = pil_img.convert("RGB").convert("L").convert("RGB")
                 pil_img = pil_img.convert("RGB", sepia_matrix).convert("RGBA")
            elif selected_filter == "Negative": pil_img = ImageOps.invert(pil_img.convert('RGB')).convert('RGBA')
            elif selected_filter == "Solarize": pil_img = ImageOps.solarize(pil_img.convert('RGB'), threshold=128).convert('RGBA')
            elif selected_filter == "Posterize": pil_img = ImageOps.posterize(pil_img.convert('RGB'), bits=4).convert('RGBA')
            elif selected_filter == "Blur": pil_img = pil_img.filter(ImageFilter.BLUR)
            elif selected_filter == "Contour": pil_img = pil_img.filter(ImageFilter.CONTOUR)
            elif selected_filter == "Detail": pil_img = pil_img.filter(ImageFilter.DETAIL)
            elif selected_filter == "Emboss": pil_img = pil_img.filter(ImageFilter.EMBOSS)
            elif selected_filter == "Edge Enhance": pil_img = pil_img.filter(ImageFilter.EDGE_ENHANCE_MORE)
            elif selected_filter == "Sharpen": pil_img = pil_img.filter(ImageFilter.SHARPEN)
            elif selected_filter == "Smooth": pil_img = pil_img.filter(ImageFilter.SMOOTH_MORE)
            update_status(f"{selected_filter} filter applied", 2000)
        return pil_img
    except Exception as e:
        showerror("Image Processing Error", f"An error occurred during transformation: {e}")
        update_status("Processing error", 3000)
        return None
def apply_flip_effect():
    global is_flipped
    if not file_path: return
    is_flipped = not is_flipped
    update_status("Flipping image...")
    transformed = _get_current_transformed_pil_image()
    if transformed: _update_canvas_image(transformed)
    update_status("Image flipped", 2000)
def apply_rotate_effect():
    global rotation_angle
    if not file_path: return
    rotation_angle = (rotation_angle + 90) % 360
    update_status("Rotating image...")
    transformed = _get_current_transformed_pil_image()
    if transformed: _update_canvas_image(transformed)
    update_status(f"Image rotated to {rotation_angle}°", 2000)
def apply_filter_effect():
    if not file_path: return
    transformed = _get_current_transformed_pil_image()
    if transformed: _update_canvas_image(transformed)
def handle_drawing(event):
    global pen_size, pen_color, file_path, canvas
    if file_path and hasattr(canvas, 'displayed_image_width') and canvas.displayed_image_width > 0:
        x, y = event.x, event.y
        if (hasattr(canvas, 'display_offset_x') and
            canvas.display_offset_x <= x < canvas.display_offset_x + canvas.displayed_image_width and
            canvas.display_offset_y <= y < canvas.display_offset_y + canvas.displayed_image_height):
            x1, y1 = (x - pen_size), (y - pen_size)
            x2, y2 = (x + pen_size), (y + pen_size)
            canvas.create_oval(x1, y1, x2, y2, fill=pen_color, outline=pen_color, width=0, tags="drawing_oval")
def select_pen_color():
    global pen_color
    new_color = colorchooser.askcolor(title="Choose Pen Color", initialcolor=pen_color)
    if new_color and new_color[1]:
        pen_color = new_color[1]
        update_status(f"Pen color changed to {pen_color}", 2000)
def clear_drawings():
    if file_path:
        canvas.delete("drawing_oval")
        update_status("Drawings cleared", 2000)
def save_edited_image():
    global file_path, canvas
    if not file_path or not hasattr(canvas, 'displayed_image_width') or canvas.displayed_image_width == 0:
        update_status("No image to save", 2000)
        return
    update_status("Preparing to save...")
    try:
        canvas_x = canvas.winfo_rootx() + int(canvas.display_offset_x)
        canvas_y = canvas.winfo_rooty() + int(canvas.display_offset_y)
        bbox = (
            canvas_x, canvas_y,
            canvas_x + canvas.displayed_image_width,
            canvas_y + canvas.displayed_image_height
        )
        image_to_save = ImageGrab.grab(bbox=bbox)
        save_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG Image", "*.png"), ("JPEG Image", "*.jpg"), ("Bitmap Image", "*.bmp")],
            initialfile=f"edited_{file_path.split('/')[-1].split('.')[0]}.png",
            title="Save Image As"
        )
        if save_path:
            update_status(f"Saving to {save_path.split('/')[-1]}...")
            image_to_save.save(save_path)
            showinfo("Save Successful", f"Image saved successfully to:\n{save_path}")
            update_status("Image saved!", 3000)
        else:
            update_status("Save cancelled", 2000)
    except Exception as e:
        showerror("Save Error", f"Failed to save image.\n{e}")
        update_status("Save failed", 3000)
root = ttk.Window(themename=APP_THEME)
root.title(APP_NAME)
root.geometry(f"{LEFT_PANEL_WIDTH + MAIN_CANVAS_WIDTH + 60}x{MAIN_CANVAS_HEIGHT + 80}")
root.resizable(False, False)
try:
    app_icon = ttk.PhotoImage(file='app_icon.png')
    root.iconphoto(False, app_icon)
except Exception: print("Warning: app_icon.png not found.")
style = ttk.Style()
style.configure('Labelframe.TLabelframe.Label', font=('Helvetica', 11, 'bold'))
main_frame = ttk.Frame(root, padding=10)
main_frame.pack(fill=BOTH, expand=True)
left_panel_frame = ttk.Frame(main_frame, width=LEFT_PANEL_WIDTH, padding=(0,0,10,0))
left_panel_frame.pack(side=LEFT, fill=Y)
left_panel_frame.pack_propagate(False)
canvas_outer_frame = ttk.Frame(main_frame, padding=(10,0,0,0))
canvas_outer_frame.pack(side=RIGHT, fill=BOTH, expand=True)
canvas = ttk.Canvas(canvas_outer_frame, width=IMAGE_DISPLAY_AREA_WIDTH, height=IMAGE_DISPLAY_AREA_HEIGHT, background=CANVAS_BG_COLOR, relief="sunken", borderwidth=1)
canvas.pack(fill=BOTH, expand=True, padx=5, pady=5)
canvas.bind("<B1-Motion>", handle_drawing)
_draw_canvas_placeholder()
def create_styled_button(parent, text, icon_name, command, style_tuple=(PRIMARY, OUTLINE), subsample_val=18):
    icon = None
    try:
        icon = ttk.PhotoImage(file=icon_name).subsample(subsample_val, subsample_val)
    except Exception: print(f"Warning: {icon_name} not found.")
    btn = ttk.Button(parent, text=text, image=icon, command=command, bootstyle=style_tuple, compound=LEFT if icon else NONE)
    if icon: btn.image = icon
    return btn
file_tools_lf = ttk.Labelframe(left_panel_frame, text=" File Operations ", padding=10)
file_tools_lf.pack(fill=X, pady=(0,15))
open_btn = create_styled_button(file_tools_lf, "Open Image", "open_icon.png", open_image_file, style_tuple=(PRIMARY))
open_btn.pack(fill=X, pady=4)
save_btn = create_styled_button(file_tools_lf, "Save Image", "save_icon.png", save_edited_image, style_tuple=(SUCCESS))
save_btn.pack(fill=X, pady=4)
transform_tools_lf = ttk.Labelframe(left_panel_frame, text=" Transformations ", padding=10)
transform_tools_lf.pack(fill=X, pady=(0,15))
flip_btn = create_styled_button(transform_tools_lf, "Flip", "flip_icon.png", apply_flip_effect, style_tuple=(INFO, OUTLINE))
flip_btn.pack(fill=X, pady=4)
rotate_btn = create_styled_button(transform_tools_lf, "Rotate", "rotate_icon.png", apply_rotate_effect, style_tuple=(INFO, OUTLINE))
rotate_btn.pack(fill=X, pady=4)
filter_tools_lf = ttk.Labelframe(left_panel_frame, text=" Image Filters ", padding=10)
filter_tools_lf.pack(fill=X, pady=(0,15))
filter_options = ["Original", "Black and White", "Sepia", "Negative", "Solarize", "Posterize", "Blur", "Contour", "Detail", "Emboss", "Edge Enhance", "Sharpen", "Smooth"]
filter_combobox = ttk.Combobox(filter_tools_lf, values=filter_options, state="readonly", bootstyle=INFO, font=('Helvetica', 10))
filter_combobox.pack(fill=X, pady=4)
filter_combobox.current(0)
filter_combobox.bind("<<ComboboxSelected>>", lambda e: apply_filter_effect())
drawing_tools_lf = ttk.Labelframe(left_panel_frame, text=" Drawing Tools ", padding=10)
drawing_tools_lf.pack(fill=X, pady=(0,15))
pen_color_btn = create_styled_button(drawing_tools_lf, "Pen Color", "color_icon.png", select_pen_color, style_tuple=(WARNING, OUTLINE))
pen_color_btn.pack(fill=X, pady=4)
erase_btn = create_styled_button(drawing_tools_lf, "Clear Drawings", "erase_icon.png", clear_drawings, style_tuple=(DANGER, OUTLINE))
erase_btn.pack(fill=X, pady=4)
status_bar_frame = ttk.Frame(root, padding=(5,5))
status_bar_frame.pack(side=BOTTOM, fill=X)
status_bar_label = ttk.Label(status_bar_frame, text="Ready", anchor=W, font=('Helvetica', 9))
status_bar_label.pack(fill=X)
def update_button_states():
    is_image_loaded = bool(file_path and hasattr(canvas, 'displayed_image_width') and canvas.displayed_image_width > 0)
    current_state = NORMAL if is_image_loaded else DISABLED
    save_btn.config(state=current_state)
    flip_btn.config(state=current_state)
    rotate_btn.config(state=current_state)
    filter_combobox.config(state=current_state)
    pen_color_btn.config(state=current_state)
    erase_btn.config(state=current_state)
    if not is_image_loaded:
        if filter_combobox.current() != 0: filter_combobox.current(0)
        _update_canvas_image(None)
update_button_states()
root.mainloop()