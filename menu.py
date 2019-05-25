#default settings
import nuke

nuke.knobDefault("EXPTool.mode", "0")
nuke.knobDefault("Viewer.freezeGuiWhenPlayBack", "1")
nuke.knobDefault("Keymix.bbox", "1")
nuke.knobDefault("Keymix.channels", "rgba")
nuke.knobDefault("Merge.bbox", "3")
nuke.knobDefault("Shuffle.label", "[value in]")
nuke.knobDefault("Blur.channels", "rgba")
nuke.knobDefault("Blur.label", "[value size] px")
nuke.knobDefault("Dilate.channels", "rgba")
nuke.knobDefault("Dilate.label", "[value size] px")
nuke.knobDefault("FilterErode.label", "[value size] px")
nuke.knobDefault("Erode.label", "[value size] px")
nuke.knobDefault("Median.label", "[value size] px")
nuke.knobDefault("Soften.channels", "rgba")
nuke.knobDefault("Soften.label", "[value size] px")
nuke.knobDefault("Sharpen.channels", "rgb")
nuke.knobDefault("Sharpen.label", "[value size] px")
nuke.knobDefault("GodRays.channels", "rgba")
nuke.knobDefault("ScanlineRender.antialiasing", "3")
nuke.knobDefault("ScanlineRender.label", "[value samples]")
nuke.knobDefault("ScanlineRender.shutteroffset", "centered")
nuke.knobDefault("Defocus.channels", "rgba")
nuke.knobDefault("Defocus.label", "[value defocus]")
nuke.knobDefault("ZDefocus2.channels", "rgba")
nuke.knobDefault("VectorBlur.channels", "rgba")
nuke.knobDefault("Dissolve.which", "1")
nuke.knobDefault("Dissolve.label", "[value which]")
nuke.knobDefault("FrameRange.label", "[value knob.first_frame] - [value knob.last_frame]")
nuke.knobDefault("Switch.which", "1")
nuke.knobDefault("Switch.label", "[value which]")
nuke.knobDefault("NoOp.hide_input", "1")
nuke.knobDefault("TimeBlur.shutteroffset", "centered")
nuke.knobDefault("Transform.shutteroffset", "centered")
nuke.knobDefault("TransformMasked.shutteroffset", "centered")
nuke.knobDefault("Expression.label", "[knob expr3")
nuke.knobDefault("Denoise2.useGPUIfAvailable", "1")
nuke.knobDefault("Mirror.Horizontal", "1")
nuke.knobDefault("Remove.operation", "keep")
nuke.knobDefault("Remove.channels", "rbga")
nuke.knobDefault("Remove.label", "[value channels")
nuke.knobDefault("Constant.channels", "rgba")
nuke.knobDefault("Retime.before", "continue")
nuke.knobDefault("Retime.after", "continue")
nuke.knobDefault("Retime.filter", "nearest")
nuke.knobDefault("Retime.label", "speed: [value speed]")
nuke.knobDefault("Gamma.channels", "rgba")
nuke.knobDefault("Colorspace.label", "value colorspace_in] -&gt; [value colorspace_out]")
nuke.knobDefault("DeepReformat.pbb", "1")
nuke.knobDefault("DeepReformat.resize", "none")
nuke.knobDefault("Multiply.label", "[value value]")
nuke.knobDefault("STMap.channels", "rgba")
nuke.knobDefault("STMap.uv", "rgb")
nuke.knobDefault("AdjBBox.numpixels","100")
nuke.knobDefault("AdjBBox.label", "[value numpixels]")



# nuke.pluginAddPath("Scripts")

# import plateLink
# nuke.menu("Nuke").addCommand('Scripts/PlateLink', 'plateLink.plateLink()', "shift+alt+v")
# import deepLink
# nuke.menu("Nuke").addCommand('Scripts/DeepLink', 'deepLink.deepLink()', "shift+alt+d")
# import cameraLink
# nuke.menu("Nuke").addCommand('Scripts/CameraLink', 'cameraLink.cameraLink()', "shift+alt+c")