class EmptyNode:
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
            },
        }
 
    RETURN_TYPES = ()
    RETURN_NAMES = ()
 
    FUNCTION = "empty"
    CATEGORY = "ecjojo_example"
 
    def empty(self):
        return ()