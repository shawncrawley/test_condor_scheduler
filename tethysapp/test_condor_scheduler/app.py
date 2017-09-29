from tethys_sdk.base import TethysAppBase, url_map_maker


class TestCondorScheduler(TethysAppBase):
    """
    Tethys app class for Test Condor Scheduler.
    """

    name = 'Test Condor Scheduler'
    index = 'test_condor_scheduler:home'
    icon = 'test_condor_scheduler/images/icon.gif'
    package = 'test_condor_scheduler'
    root_url = 'test-condor-scheduler'
    color = '#f39c12'
    description = 'This app does stuff you could not even dream of.'
    tags = ''
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='test-condor-scheduler',
                controller='test_condor_scheduler.controllers.home'
            ),
            UrlMap(
                name='run_job',
                url='test-condor-scheduler/run-job',
                controller='test_condor_scheduler.controllers.run_job'
            ),
            UrlMap(
                name='job_table',
                url='test-condor-scheduler/job-table',
                controller='test_condor_scheduler.controllers.job_table'
            ),
        )

        return url_maps

    def job_templates(self):
        from tethys_sdk.jobs import CondorJobDescription, CondorJobTemplate
        from tethys_sdk.compute import get_scheduler
        scheduler = get_scheduler('send_to_nathan')

        job_description = CondorJobDescription(
            condorpy_template_name='vanilla_transfer_files',
            remote_input_files=['$(APP_WORKSPACE)/hello_world.py'],
            executable='hello_world.py',
            transfer_input_files=['../hello_world.py'],
            transfer_output_files=['output.py']
        )

        job_templates = (
            CondorJobTemplate(
                name='test',
                job_description=job_description,
                scheduler=scheduler
            ),
        )

        return job_templates
