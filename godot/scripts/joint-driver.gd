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


# Called when the node enters the scene tree for the first time.
func _ready():
	pass


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	# Update joint positions here
	$"neck/shoulder-fl".rotation 			= Vector3(0, PI, fl.x)
	$"neck/shoulder-fl/hip".rotation		= Vector3(-fl.y, 0, 0)
	$"neck/shoulder-fl/hip/knee".rotation 	= Vector3(fl.z, 0, 0)
	$"neck/shoulder-fr".rotation 			= Vector3(0, PI, PI - fr.x)
	$"neck/shoulder-fr/hip".rotation		= Vector3(fr.y, 0, 0)
	$"neck/shoulder-fr/hip/knee".rotation 	= Vector3(-fr.z, 0, 0)
	$"body/shoulder-br".rotation 			= Vector3(0, PI, PI - br.x)
	$"body/shoulder-br/hip".rotation		= Vector3(br.y, 0, 0)
	$"body/shoulder-br/hip/knee".rotation 	= Vector3(-br.z, 0, 0)
	$"body/shoulder-bl".rotation 			= Vector3(0, PI, bl.x)
	$"body/shoulder-bl/hip".rotation		= Vector3(-bl.y, 0, 0)
	$"body/shoulder-bl/hip/knee".rotation 	= Vector3(bl.z, 0, 0)
	$"neck".rotation						= Vector3(0, 0, neck)
	pass
