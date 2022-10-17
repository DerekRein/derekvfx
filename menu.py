#default settings
import nuke


# TIME
nuke.knobDefault("FrameRange.label", "[value knob.first_frame] - [value knob.last_frame]")
nuke.knobDefault("TimeBlur.shutteroffset", "centered")
nuke.knobDefault("Retime.before", "continue")
nuke.knobDefault("Retime.after", "continue")
nuke.knobDefault("Retime.filter", "nearest")
nuke.knobDefault("Retime.label", "speed: [value speed]")
# CHANNELS
nuke.knobDefault("Remove.operation", "keep")
nuke.knobDefault("Remove.channels", "rbga")
nuke.knobDefault("Remove.label", "[value channels]")
nuke.knobDefault("Shuffle.label", "[value in]")

# COLOR CORRECT
nuke.knobDefault("EXPTool.mode", "0")
nuke.knobDefault("Gamma.channels", "rgba")
nuke.knobDefault("Colorspace.label", "[value colorspace_in] - [value colorspace_out]")
nuke.knobDefault("Colorspace.colorspace_out", "AlexaV3LogC")
nuke.knobDefault("Multiply.label", "[value value]")
nuke.knobDefault("Saturation.label", "[value saturation]")
nuke.knobDefault("Saturation.saturation", "0")
# CONVOLUTIONS
nuke.knobDefault("Denoise2.useGPUIfAvailable", "1")
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
nuke.knobDefault("Defocus.channels", "rgba")
nuke.knobDefault("Defocus.label", "[value defocus]")
nuke.knobDefault("ZDefocus2.channels", "rgba")
nuke.knobDefault("VectorBlur.channels", "rgba")

# MERGE
nuke.knobDefault("Switch.which", "1")
nuke.knobDefault("Switch.label", "[value which]")
nuke.knobDefault("Dissolve.which", "1")
nuke.knobDefault("Dissolve.label", "[value which]")
nuke.knobDefault("Keymix.bbox", "1")
nuke.knobDefault("Keymix.channels", "rgba")
nuke.knobDefault("Merge.bbox", "3")
# TRANSFORM
nuke.knobDefault("Transform.shutteroffset", "centered")
nuke.knobDefault("TransformMasked.shutteroffset", "centered")
nuke.knobDefault("CornerPin2D.shutteroffset", "centered")
nuke.knobDefault("Tracker4.shutteroffset", "centered")
nuke.knobDefault("Card3D.shutteroffset", "centered")
nuke.knobDefault("Reconcile3D.shutteroffset", "centered")
nuke.knobDefault("Mirror.Horizontal", "1")
nuke.knobDefault("Mirror2.flop", "1")
# 3D
nuke.knobDefault("ScanlineRender.antialiasing", "3")
nuke.knobDefault("ScanlineRender.label", "[value samples]")
nuke.knobDefault("ScanlineRender.shutteroffset", "centered")
# MISC
nuke.knobDefault("Expression.label", "[knob expr3]")
nuke.knobDefault("Viewer.freezeGuiWhenPlayBack", "1")
nuke.knobDefault("NoOp.hide_input", "1")
nuke.knobDefault("DeepReformat.pbb", "1")
nuke.knobDefault("DeepReformat.resize", "none")
nuke.knobDefault("STMap.channels", "rgba")
nuke.knobDefault("STMap.uv", "rgb")
nuke.knobDefault("AdjBBox.numpixels", "100")
nuke.knobDefault("AdjBBox.label", "[value numpixels]")
nuke.knobDefault("Constant.channels", "rgba")
nuke.knobDefault("VectorDistort.label", "REF: [value reference_frame]")

nuke.menu("Nuke").addCommand('Scripts/Align', 'align.aligner()', "shift+alt+a")
nuke.menu("Nuke").addCommand('Scripts/Reveal File', 'sb_revealInFileBrowser.sb_revealInFileBrowser()')
nuke.menu("Nuke").addCommand('Scripts/Convert Corner Pin', 'sb_convertCornerPin.main()')
nuke.menu("Nuke").addCommand('Scripts/Matrix Inverter', 'matrixInverter.main()')
nuke.menu("Nuke").addCommand('Scripts/Mirror Nodes', 'mirrorNodes.main()')
nuke.menu("Nuke").addCommand('Scripts/Delete Viewers', 'sb_deleteViewers.sb_deleteViewers()')
nuke.menu("Nuke").addCommand('Scripts/PlateLink', 'Links.plate_link()', "shift+alt+v")
nuke.menu("Nuke").addCommand('Scripts/DeepLink', 'Links.deep_link()', "shift+alt+d")
nuke.menu("Nuke").addCommand('Scripts/CameraLink', 'Links.camera_link()', "shift+alt+c")
nuke.menu("Nuke").addCommand("Edit/Node/Align/Left", 'W_smartAlign.alignNodes("left")', "Alt+left", shortcutContext=2)
nuke.menu("Nuke").addCommand("Edit/Node/Align/Right", 'W_smartAlign.alignNodes("right")', "Alt+right",
                             shortcutContext=2)
nuke.menu("Nuke").addCommand("Edit/Node/Align/Up", 'W_smartAlign.alignNodes("up")', "Alt+up", shortcutContext=2)
nuke.menu("Nuke").addCommand("Edit/Node/Align/Down", 'W_smartAlign.alignNodes("down")', "Alt+down", shortcutContext=2)

# nuke.pluginAddPath("Scripts")

# import plateLink
# nuke.menu("Nuke").addCommand('Scripts/PlateLink', 'plateLink.plateLink()', "shift+alt+v")
# import deepLink
# nuke.menu("Nuke").addCommand('Scripts/DeepLink', 'deepLink.deepLink()', "shift+alt+d")
# import cameraLink
# nuke.menu("Nuke").addCommand('Scripts/CameraLink', 'cameraLink.cameraLink()', "shift+alt+c")