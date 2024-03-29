import pygame, json, os, gameslib

def load_image(path: str, colorkey: gameslib.Color=None, scale: int=1):
	"""Loads image from a given path.

	Parameters
	----------
	path : str
		Path to file
	colorkey: (int, int, int)
		Transparent color. None by default
	scale: int
		Scale ratio. Must be geather than 0, 1 by default (no scale)"""

	image = pygame.image.load(path)

	if colorkey is None:
		image.convert_alpha()

	else:
		image.convert()
		print(colorkey)
		image.set_colorkey(colorkey)

	return scale_image(image, scale)

def create_image(size: gameslib.Size, colorkey: gameslib.Color=None, bg_color: gameslib.Color=(0, 0, 0), scale: int=1):
	"""Returns a new image with the given size.
	
	Parameters
	----------
	size : (int, int)
		Width and height of the new image
	colorkey: (int, int, int)
		Transparent color. None by default
	bg_color: (int, int, int) or (int, int, int, int)
		color to fill the created image
	scale: int
		Scale ratio. Must be geather than 0, 1 by default (no scale)"""

	if colorkey is None:
		image = pygame.Surface(size, pygame.SRCALPHA).convert_alpha()

	else:
		image = pygame.Surface(size).convert()
		image.set_colorkey(colorkey)

	image.fill(bg_color)

	return scale_image(image, scale)

def scale_image(image: pygame.Surface, scale: int):
	"""Scales image.

	Parameters
	----------
	scale: int
		Scale ratio. Must be geather than 0, 1 by default (no scale)"""

	if scale > 0:
		w, h = image.get_size()
		image = pygame.transform.scale(image, (int(w * scale), int(h * scale)))

	return image

def load_frames_info(path: str, file_name: str, scale: int=1):
	"""Loads sprite frames info from file

	Parameters
	----------
	path : str
		Path to file
	scale: int
		Scale ratio. Must be geather than 0, 1 by default (no scale)"""

	frames_path = os.path.join(path, file_name + '.data')
	file = open(frames_path)
	src_frames = json.load(file)
	file.close()

	frames = {}
	for key in list(src_frames.keys()):
		frames[key] = []
		for frame in src_frames[key]:
			x, y, w, h = tuple(frame)
			x, y, w, h = int(x * scale), int(y * scale), int(w * scale), int(h * scale)
			frames[key].append(pygame.Rect(x, y, w, h))

	# loads sprites source
	source_path = os.path.join(path, file_name + '.png')
	source = load_image(source_path, scale=scale)

	return source, frames

def scale_pos(pos: gameslib.Pos, scale: int=1):
	"""Scales a postion coordinates (x, y) using the given scale.

	Parameters
	----------
	pos : (int, int)
		Position to scale
	scale: int
		Scale ratio. Must be geather than 0, 1 by default (no scale)"""

	if scale > 0:
		x, y = pos
		pos = (int(x * scale), int(y * scale))

	return pos

def scale_rects(rects: gameslib.Rects | pygame.Rect, scale: int=1):
	"""Scales a rect (x, y, w, h) using the given scale.

	Parameters
	----------
	rects : [(int, int, intm int)] or (int, int, intm int)
		Rectangles or frames to scale
	scale: int
		Scale ratio. Must be geather than 0, 1 by default (no scale)"""

	if scale > 0:

		if not isinstance(rects, list):
			rects = [rects]

		for i in range(len(rects)):
			x, y, w, h = rects[i]
			rects[i] = int(x * scale), int(y * scale), int(w * scale), int(h * scale)

	return rects
