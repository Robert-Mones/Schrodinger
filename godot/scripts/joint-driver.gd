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

# Reference to joint Spatial nodes
var joints: Array


# Called when the node enters the scene tree for the first time.
func _ready():
	joints.append_array([
		$"shoulder-fl",
		$"shoulder-fl/hip",
		$"shoulder-fl/hip/knee",
		$"shoulder-fr",
		$"shoulder-fr/hip",
		$"shoulder-fr/hip/knee",
		$"shoulder-br",
		$"shoulder-br/hip",
		$"shoulder-br/hip/knee",
		$"shoulder-bl",
		$"shoulder-bl/hip",
		$"shoulder-bl/hip/knee",
		$"body/neck"
	])


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	# Update joint positions here
	pass
