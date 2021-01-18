# coding=utf-8
from __future__ import absolute_import

### (Don't forget to remove me)
# This is a basic skeleton for your plugin's __init__.py. You probably want to adjust the class name of your plugin
# as well as the plugin mixins it's subclassing from. This is really just a basic skeleton to get you started,
# defining your plugin as a template plugin, settings and asset plugin. Feel free to add or remove mixins
# as necessary.
#
# Take a look at the documentation on what other plugin mixins are available.

import octoprint.plugin

class StreamOverlayPlugin(
	octoprint.plugin.SettingsPlugin,
	octoprint.plugin.TemplatePlugin,
	octoprint.plugin.UiPlugin):

	def get_settings_defaults(self):
		return dict(
			hsize=False,
			vsize=False
		)

	def get_template_configs(self):
		return [
			dict(type="navbar", custom_bindings=False),
		]

	def get_template_vars(self):
		return dict(
			hsize=self._settings.get(["hsize"]),
			vsize=self._settings.get(["vsize"])
		)

	def will_handle_ui(self, request):
		return 'stream_overlay' in request.args

	def on_ui_render(self, now, request, render_kwargs):
		from flask import make_response, render_template
		render_kwargs['settings'] = self._settings
		return make_response(render_template("stream_overlay.jinja2", **render_kwargs))

	def get_update_information(self):
		# https://docs.octoprint.org/en/master/bundledplugins/softwareupdate.html
		return dict(
			stream_overlay=dict(
				displayName="Stream Overlay Plugin",
				displayVersion=self._plugin_version,

				type="github_release",
				user="daschu117",
				repo="octoprint-stream-overlay",
				current=self._plugin_version,

				pip="https://github.com/daschu117/octoprint-stream-overlay/archive/{target_version}.zip"
			)
		)


__plugin_name__ = "Stream Overlay Plugin"
__plugin_pythoncompat__ = ">=2.7,<4" # python 2 and 3
__plugin_implementation__ = StreamOverlayPlugin()

"""
def __plugin_load__():
	global __plugin_implementation__
	__plugin_implementation__ = StreamOverlayPlugin()

	global __plugin_hooks__
	__plugin_hooks__ = {
		"octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
	}

"""
