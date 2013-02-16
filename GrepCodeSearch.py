import sublime, sublime_plugin

class GrepCodeSearchCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            word = self.view.word(region)
            if not word.empty():
                url = "http://grepcode.com/search/?query=%s" % self.view.substr(word)
                sublime.active_window().run_command('open_url', {"url": url})
