from argparse import ArgumentParser
from logging import getLogger

from baelfire.application.application import Application
from baelfire.application.commands.graph.graph import Graph

from rbh.core import KbhCore

log = getLogger(__name__)


class BaseApplication(Application):
    core_cls = KbhCore
    tasks = dict()
    tasks_help = None

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
            'tasks',
            help=self.tasks_help,
            choices=self.tasks.keys(),
        )
        tasks.add_argument(
            '-g',
            '--graph',
            dest='graph',
            help='Draw task dependency graph.',
            action="store_true",
        )
        return tasks

    def run_command_or_print_help(self, args):
        if args.tasks:
            task = self.get_task(args.tasks, args)
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

    def get_task(self, task, args):
        return self.tasks[task](self.core_cls())
