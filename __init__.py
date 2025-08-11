"""
Relative Frame Display Addon for Blender

This addon displays the current frame number relative to the start of the timeline 
playback range directly in the 3D viewport. Useful for animators who want to see 
their position relative to animation sequences rather than absolute frame numbers.

Author: Eaxum
Version: 1.2
Compatible with: Blender 4.0+
"""

bl_info = {
    "name": "Relative Frame Display",
    "author": "Eaxum",
    "version": (1, 2),
    "blender": (4, 0, 0),
    "location": "3D Viewport > View Menu & Animation Panel",
    "description": "Displays the current frame number relative to the start of the timeline playback range in the 3D viewport",
    "category": "Animation",
    "doc_url": "",
    "tracker_url": "",
    "support": "COMMUNITY",
}

import bpy
import blf
from bpy.types import Operator, Panel
from bpy.props import BoolProperty

# Global variables to track if the display is enabled and store the draw handler
display_enabled = False
draw_handler = None

def draw_viewport_text():
    """Draw function for viewport text overlay"""
    if not display_enabled:
        return
    
    try:
        context = bpy.context
        if not context or not context.scene:
            return
            
        scene = context.scene
        start_frame = scene.frame_start
        current_frame = scene.frame_current
        relative_frame = current_frame - start_frame + 1
        
        # Enable blending for text rendering
        import gpu
        gpu.state.blend_set('ALPHA')
        
        # Position in bottom-left corner
        font_id = 0
        x_pos = 20  # Left margin
        y_pos = 80  # Bottom margin
        
        # Draw main relative frame text
        blf.position(font_id, x_pos, y_pos, 0)
        blf.size(font_id, 32)  # Medium size for main text
        blf.color(font_id, 1.0, 1.0, 1.0, 0.9)  # White with slight transparency
        
        text = f"Relative Frame: {relative_frame}"
        blf.draw(font_id, text)
        
        # Draw additional info below in smaller, subdued text
        blf.position(font_id, x_pos, y_pos - 25, 0)
        blf.size(font_id, 16)
        blf.color(font_id, 0.7, 0.7, 0.7, 0.8)  # Light gray with transparency
        info_text = f"Current: {current_frame} / Start: {start_frame}"
        blf.draw(font_id, info_text)
        
    except Exception as e:
        print(f"Error in draw_viewport_text: {e}")

class ANIM_OT_toggle_relative_frame(Operator):
    """Toggle relative frame display in the 3D viewport"""
    bl_idname = "anim.toggle_relative_frame"
    bl_label = "Toggle Relative Frame Display"
    bl_description = "Toggle the relative frame counter in the 3D viewport"
    
    def execute(self, context):
        global display_enabled, draw_handler
        
        try:
            if display_enabled:
                # Remove the viewport display
                if draw_handler:
                    bpy.types.SpaceView3D.draw_handler_remove(draw_handler, 'WINDOW')
                    draw_handler = None
                display_enabled = False
                self.report({'INFO'}, "Relative Frame viewport display disabled")
            else:
                # Add the viewport display
                draw_handler = bpy.types.SpaceView3D.draw_handler_add(
                    draw_viewport_text, (), 'WINDOW', 'POST_PIXEL'
                )
                display_enabled = True
                self.report({'INFO'}, "Relative Frame viewport display enabled")
            
            # Force viewport update
            for area in context.screen.areas:
                if area.type == 'VIEW_3D':
                    area.tag_redraw()
            
            return {'FINISHED'}
            
        except Exception as e:
            self.report({'ERROR'}, f"Failed to toggle display: {str(e)}")
            print(f"Error in execute: {e}")
            return {'CANCELLED'}

class ANIM_PT_relative_frame_panel(Panel):
    """Panel in the Animation workspace"""
    bl_label = "Relative Frame Display"
    bl_idname = "ANIM_PT_relative_frame"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Animation"
    
    def draw(self, context):
        layout = self.layout
        
        # Current status
        scene = context.scene
        start_frame = scene.frame_start
        current_frame = scene.frame_current
        relative_frame = current_frame - start_frame + 1
        
        col = layout.column()
        col.label(text="Timeline Info:")
        col.label(text=f"Start Frame: {start_frame}")
        col.label(text=f"Current Frame: {current_frame}")
        col.label(text=f"Relative Frame: {relative_frame}")
        
        layout.separator()
        
        # Toggle button
        if display_enabled:
            layout.operator("anim.toggle_relative_frame", text="Hide Viewport Display", icon='HIDE_ON')
        else:
            layout.operator("anim.toggle_relative_frame", text="Show Viewport Display", icon='HIDE_OFF')

def menu_func(self, context):
    """Add to Animation menu"""
    self.layout.operator("anim.toggle_relative_frame")

# Registration
classes = (
    ANIM_OT_toggle_relative_frame,
    ANIM_PT_relative_frame_panel,
)

def register():
    """Register all addon classes and handlers"""
    try:
        for cls in classes:
            bpy.utils.register_class(cls)
        
        # Add to Animation menu
        bpy.types.VIEW3D_MT_view.append(menu_func)
        
        print("Relative Frame Display addon registered successfully")
        
    except Exception as e:
        print(f"Error registering Relative Frame Display addon: {e}")

def unregister():
    """Unregister all addon classes and clean up"""
    global display_enabled, draw_handler
    
    try:
        # Clean up viewport display if active
        if display_enabled and draw_handler:
            bpy.types.SpaceView3D.draw_handler_remove(draw_handler, 'WINDOW')
            draw_handler = None
            display_enabled = False
        
        # Remove from menu
        bpy.types.VIEW3D_MT_view.remove(menu_func)
        
        # Unregister classes in reverse order
        for cls in reversed(classes):
            bpy.utils.unregister_class(cls)
            
        print("Relative Frame Display addon unregistered successfully")
        
    except Exception as e:
        print(f"Error unregistering Relative Frame Display addon: {e}")

if __name__ == "__main__":
    register()
