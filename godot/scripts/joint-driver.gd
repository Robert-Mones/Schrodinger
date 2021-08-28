#tool
extends Spatial



# Constant joint offsets
const offsets: Array = [
#   shldr hip   knee
	0,    0,    0,  # FL
	0,    0,    0,  # FR
	180,  0,    0,  # BR
	-180, 0,    0,  # BL
	180             # Neck
]

# Joint setpoints
export var fl: Vector3
export var fr: Vector3
export var br: Vector3
export var bl: Vector3
export var neck: float

export var A: float = 0.17
export var B: float = 0.1414 #0.13
export var hipOffset: float = 0.14916 #0.1
export var C: float = 0.055

export var L1: float = .17
export var L2: float = .14
export var L2B: float = .02
export var L3: float = .06
export var legRoot: Vector3

# Input scaling coefficients
export var neckCoef: float = -1.0
export var legCoef: float = 2.0

var circleTime: float = 0.0

func updateA(text):
	A = float(text)

func updateB(text):
	B = float(text)

func updateHipOffset(text):
	hipOffset = float(text)

func updateC(text):
	C = float(text)

# Called when the node enters the scene tree for the first time.
func _ready():
	pass

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	# Take user input
	var triggerInput = Input.get_action_strength("trigger_right") - Input.get_action_strength("trigger_left")
	var leftXInput = Input.get_action_strength("left_right") - Input.get_action_strength("left_left")
	var leftYInput = Input.get_action_strength("left_up") - Input.get_action_strength("left_down")
	var rightXInput = Input.get_action_strength("right_right") - Input.get_action_strength("right_left")
	var rightYInput = Input.get_action_strength("right_up") - Input.get_action_strength("right_down")
	var resetInput = Input.is_action_pressed("ui_cancel")
	var upInput = Input.is_action_pressed("ui_up")
	var downInput = Input.is_action_pressed("ui_down")
	
	# Process user input
	#neck += neckCoef * triggerInput * delta
	
	#$"target_endpoint".translation.x += legCoef * leftXInput * delta
	#$"target_endpoint".translation.y += legCoef * rightYInput * delta
	#$"target_endpoint".translation.z -= legCoef * leftYInput * delta
	#print($"target_endpoint".translation)
	
	br.x += legCoef * leftYInput * delta
	br.y += legCoef * rightYInput * delta
	br.z += legCoef * triggerInput * delta
	print(br)
	
	if upInput:
		br.z = PI/2
	elif downInput:
		br.z = -PI/2
	
	if resetInput:
		br = Vector3(0.0, 0.0, 0.0)
		neck = 0.0
	
	# Update joint positions here
	$"neck/shoulder-fl".rotation 			= Vector3(0, PI, fl.z)
	$"neck/shoulder-fl/hip".rotation		= Vector3(-fl.y, 0, 0)
	$"neck/shoulder-fl/hip/knee".rotation 	= Vector3(fl.x, 0, 0)
	$"neck/shoulder-fr".rotation 			= Vector3(0, PI, PI - fr.z)
	$"neck/shoulder-fr/hip".rotation		= Vector3(fr.y, 0, 0)
	$"neck/shoulder-fr/hip/knee".rotation 	= Vector3(-fr.x, 0, 0)
	$"body/shoulder-br".rotation 			= Vector3(0, PI, PI - br.z)
	$"body/shoulder-br/hip".rotation		= Vector3(br.y, 0, 0)
	$"body/shoulder-br/hip/knee".rotation 	= Vector3(-br.x, 0, 0)
	$"body/shoulder-bl".rotation 			= Vector3(0, PI, bl.z)
	$"body/shoulder-bl/hip".rotation		= Vector3(-bl.y, 0, 0)
	$"body/shoulder-bl/hip/knee".rotation 	= Vector3(bl.x, 0, 0)
	$"neck".rotation						= Vector3(0, 0, neck)
	
	#var endpointPos = Vector3(
	#	(L1 * (cos(bl.x)*sin(br.y) + sin(br.x)*cos(br.y)) - L2*sin(br.y) + L2B*cos(br.y))*sin(br.z) + L3*cos(br.z),
	#	(-L1 * (cos(bl.x)*sin(br.y) + sin(br.x)*cos(br.y))) + L3*sin(br.y) - L2B*cos(br.y),
	#	((-L1 * (cos(bl.x)*sin(br.y) + sin(br.x)*cos(br.y))) + L2*sin(br.y) - L2B*cos(br.y))*cos(br.z) + L3*sin(br.z)
	#)
	var actualY = br.y + hipOffset
	var l = (B * sin(actualY)) + (A * sin(br.x - br.y))
	var endpointPos = Vector3(
		(C * cos(br.z)) + (l * sin(br.z)),
		(C * sin(br.z)) - (l * cos(br.z)),
		(B * cos(actualY)) - (A * cos(br.x - br.y))
	)
	$"test_endpoint".translation = legRoot + endpointPos
	#$"test_endpoint".translation = legRoot
	
	circleTime += delta
	if circleTime > 0.5:
		circleTime = 0.0
		
	
	pass
