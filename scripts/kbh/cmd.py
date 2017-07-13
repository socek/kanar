from argparse import ArgumentParser
from logging import getLogger

from baelfire.application.application import Application
from baelfire.application.commands.graph.graph import Graph

from kbh.containers import RunBackendContainer
from kbh.containers import RunFrontendContainer
from kbh.containers import RunNginxContainer
from kbh.core import KbhCore

log = getLogger(__name__)


class KbhApplication(Application):
    core_cls = KbhCore

    containers = {
        'backend': RunBackendContainer,
        'nginx': RunNginxContainer,
        'frontend': RunFrontendContainer,
    }

    def create_parser(self):
        self.parser = ArgumentParser()
        self._add_task_group()
        self._add_logging_group()
        self._add_other_group()

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
            task = self.get_task(args.container)
            try:
                try:
                    task.run()
                finally:
                    report_path = task.save_report()
                    if args.graph:
                        Graph(report_path).render()
            except:
                log.error('Error in %s' % (report_path,))
                raise

        elif args.graph_file:
            Graph(args.graph_file).render()
        else:
            if not self._run_missing_command():
                self.parser.print_help()

    def get_task(self, container):
        return self.containers[container](self.core_cls())


def run():
    KbhApplication().run()
