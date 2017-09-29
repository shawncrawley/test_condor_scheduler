from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tethys_sdk.gizmos import Button


@login_required()
def home(request):
    """
    Controller for the app home page.
    """
    save_button = Button(
        display_text='',
        name='save-button',
        icon='glyphicon glyphicon-floppy-disk',
        style='success',
        attributes={
            'data-toggle': 'tooltip',
            'data-placement': 'top',
            'title': 'Save',
            'onclick': 'run_job();'
        }
    )

    edit_button = Button(
        display_text='',
        name='edit-button',
        icon='glyphicon glyphicon-edit',
        style='warning',
        attributes={
            'data-toggle':'tooltip',
            'data-placement':'top',
            'title':'Edit'
        }
    )

    remove_button = Button(
        display_text='',
        name='remove-button',
        icon='glyphicon glyphicon-remove',
        style='danger',
        attributes={
            'data-toggle':'tooltip',
            'data-placement':'top',
            'title':'Remove'
        }
    )

    previous_button = Button(
        display_text='Previous',
        name='previous-button',
        attributes={
            'data-toggle':'tooltip',
            'data-placement':'top',
            'title':'Previous'
        }
    )

    next_button = Button(
        display_text='Next',
        name='next-button',
        attributes={
            'data-toggle':'tooltip',
            'data-placement':'top',
            'title':'Next'
        }
    )

    context = {
        'save_button': save_button,
        'edit_button': edit_button,
        'remove_button': remove_button,
        'previous_button': previous_button,
        'next_button': next_button
    }

    return render(request, 'test_condor_scheduler/home.html', context)


def run_job(request):
    from tethysapp.test_condor_scheduler.app import TestCondorScheduler as ThisApp

    if request.method == 'GET':
        import pdb
        pdb.set_trace()
        job_manager = ThisApp.get_job_manager()
        job = job_manager.create_job(name='test_job_1', user=request.user, template_name='test',
                                     description='First stab at submitting a job to a remote computer.')
        job.save()
        job.execute()

        return job_table(request, job_manager)


def job_table(request, job_manager=None):
    from tethysapp.test_condor_scheduler.app import TestCondorScheduler as ThisApp
    from tethys_sdk.gizmos import JobsTable

    if not job_manager:
        job_manager = ThisApp.get_job_manager()

    jobs = job_manager.list_jobs()

    jobs_table_options = JobsTable(
        jobs=jobs,
        column_fields=('id', 'name', 'creation_time', 'execute_time', 'run_time'),
        hover=True,
        striped=False,
        bordered=False,
        condensed=False,
    )

    context = {
        'jobs_table_options': jobs_table_options
    }

    return render(request, 'test_condor_scheduler/job_table.html', context)
