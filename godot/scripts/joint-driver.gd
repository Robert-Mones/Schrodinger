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
export var root: NodePath
export var target: NodePath

export var fr: Vector3
export var br: Vector3
export var bl: Vector3
export var neck: float

# Leg Lengths
const a = 0.055
const b = 0.134503
const c = 0.148

func algo():
	# Calculate the relative (x,y,z) for the desired 
	var offset = (get_node(target) as Spatial).translation - (get_node(root) as Spatial).translation;
	
	var abc = offset.length();
	var bc = sqrt( pow(abc,2)-pow(a,2) )
	var C = acos( (pow(b,2)+pow(c,2)-pow(bc,2)) / (2*b*c) )
	var B = asin( -offset.z / bc ) + PI/2 - asin( (c*sin(C)) / bc )
	var abc_proj = sqrt(pow(offset.x, 2) + pow(offset.y, 2))
	var A = acos(a/abc_proj) - acos(offset.x/abc_proj)
	#var A = atan( (bc*cos(B)) / a ) + atan(offset.x / offset.y) - PI/2
	fr = Vector3(C-.15, B-.15, A)
	
	print(bc)

# Called when the node enters the scene tree for the first time.
func _ready():
	pass

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	algo();
	
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
	
	pass
