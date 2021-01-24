# coding=utf-8
from __future__ import absolute_import
import octoprint.plugin


class StreamOverlayPlugin(octoprint.plugin.UiPlugin, octoprint.plugin.TemplatePlugin):

	def _get_widget(self, name):
		# TODO: security check this
		return "widgets/%s.jinja2" % name

	def will_handle_ui(self, request):
		print(f"uhh {request.args}")
		self._logger.info(f"uhhx {request.args}")
		return 'stream_overlay' in request.args

	def on_ui_render(self, now, request, render_kwargs):
		from flask import make_response, render_template
		#render_kwargs['settings'] = self._settings
		widget = request.args['stream_overlay']
		if widget and widget != 'default':
			t = self._get_widget(widget)
			return make_response(render_template(t, **render_kwargs))
		return make_response(render_template("stream_overlay_main.jinja2", **render_kwargs))

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
