from argparse import ArgumentParser
from logging import getLogger

from baelfire.application.application import Application
from baelfire.application.commands.graph.graph import Graph

from kbh.core import KbhCore

log = getLogger(__name__)


class KbhApplication(Application):
    core_cls = KbhCore

    containers = {
        'backend': 'kbh.docker:BackendContainer',
    }

    def create_parser(self):
        self.parser = ArgumentParser()
        self._add_task_group()
        self._add_logging_group()

    def _add_task_group(self):
        tasks = self.parser.add_argument_group(
            'Tasks',
            'Project related options',
        )

        tasks.add_argument(
            '-c',
            '--container',
            dest='container',
            help='Start container.',
            choices=self.containers.keys(),
        )
        tasks.add_argument(
            '-g',
            '--graph',
            dest='graph',
            help='Draw task dependency graph.',
            action="store_true",
        )

    def run_command_or_print_help(self, args):
        if args.container:
            task = self._get_task(args)
            try:
                try:
                    task.run()
                finally:
                    report_path = task.save_report()
            except:
                log.error('Error in %s' % (report_path,))
                raise
            if args.graph:
                Graph(report_path).render()
        else:
            self.parser.print_help()

    def _get_task(self, args):
        url = self.containers[args.container]
        task = self.import_task(url)
        return task(self.core_cls())


def run():
    KbhApplication().run()
