tool
extends Spatial


# Declare member variables here. Examples:
export var target : NodePath
export var offset := Vector3(0, 0, 0)
export var lookAtTarget := true

var targetNode : Spatial = null

# Called when the node enters the scene tree for the first time.
func _ready():
	pass

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	if (targetNode == null):
		targetNode = get_node(target) as Spatial
		return
	
	var targetPos = targetNode.get_parent_spatial().to_global(targetNode.translation)
	translation = targetPos + offset;
	
	if (lookAtTarget):
		look_at(targetPos, Vector3(0,1,0))
