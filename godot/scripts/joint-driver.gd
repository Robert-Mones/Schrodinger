tool
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

export var L1: float = .17
export var L2: float = .14
export var L2B: float = .02
export var L3: float = .06
export var legRoot: Vector3



# Called when the node enters the scene tree for the first time.
func _ready():
	pass


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
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
	
	var endpointPos = Vector3(
		(L1 * (cos(bl.x)*sin(br.y) + sin(br.x)*cos(br.y)) - L2*sin(br.y) + L2B*cos(br.y))*sin(br.z) + L3*cos(br.z),
		(-L1 * (cos(bl.x)*sin(br.y) + sin(br.x)*cos(br.y))) + L3*sin(br.y) - L2B*cos(br.y),
		((-L1 * (cos(bl.x)*sin(br.y) + sin(br.x)*cos(br.y))) + L2*sin(br.y) - L2B*cos(br.y))*cos(br.z) + L3*sin(br.z)
	)
	$"test_endpoint".translation = legRoot + endpointPos
	#$"test_endpoint".translation = legRoot
	pass
