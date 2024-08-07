from celery import shared_task
from .models import ComputationStatus, Notification, Client
from .computations.permanent_computations import PermanentComputations
from .interim.dashboard_computations import generate_automated_suggestions, performance_dashboard
from .interim.performance_analysis import forecast_vs_actual_comparison, probability_analysis, process_progress_tracking
from .interim.statistical_analysis import calculate_advanced_stats, calculate_aggregated_views, calculate_basic_stats
from .interim.experiment_analysis import ab_test_analysis, difference_in_differences
from .interim.data_export import bulk_export_data, prepare_data_for_bulk_import

@shared_task
def run_computations(tenant_id, metric_ids):
    try:
        computation_status = ComputationStatus.objects.create(tenant_id=tenant_id, status='IN_PROGRESS')
        tenant = Client.objects.get(id=tenant_id)
        PermanentComputations(metric_ids, tenant).run_all_computations()
        computation_status.status = 'COMPLETED'
        computation_status.save()
        Notification.objects.create(
            tenant_id=tenant_id,
            message='Computations completed successfully.'
        )
    except Exception as e:
        computation_status.status = 'FAILED' 
        computation_status.error_message = str(e)
        computation_status.save()
        Notification.objects.create(
            tenant_id=tenant_id,
            message='Computations failed with error: {e}'.format(e=e)
        )

@shared_task
def run_long_computation(metric_id, computation_type, **kwargs):
    if computation_type == 'automated_suggestions':
        return generate_automated_suggestions(metric_id)
    elif computation_type == 'performance_dashboard':
        current_date = kwargs.get('current_date')
        return performance_dashboard(metric_id, current_date)
    elif computation_type == 'bulk_export':
        start_date = kwargs.get('start_date')
        end_date = kwargs.get('end_date')
        data_type = kwargs.get('data_type', 'raw')
        return bulk_export_data(metric_id, start_date, end_date, data_type)
    elif computation_type == 'prepare_bulk_import':
        sheet_url = kwargs.get('sheet_url')
        return prepare_data_for_bulk_import(sheet_url)
    elif computation_type == 'advanced_stats':
        return calculate_advanced_stats(metric_id)
    elif computation_type == 'aggregated_views':
        return calculate_aggregated_views(metric_id)
    elif computation_type == 'basic_stats':
        return calculate_basic_stats(metric_id)
    elif computation_type == 'forecast_comparison':
        return forecast_vs_actual_comparison(metric_id)
    elif computation_type == 'probability_analysis':
        return probability_analysis(metric_id)
    elif computation_type == 'progress_tracking':
        return process_progress_tracking(metric_id)
    elif computation_type == 'ab_test':
        control_group = kwargs.get('control_group')
        treatment_group = kwargs.get('treatment_group')
        return ab_test_analysis(metric_id, control_group, treatment_group)
    elif computation_type == 'difference_in_differences':
        pre_period = kwargs.get('pre_period')
        post_period = kwargs.get('post_period')
        control_group = kwargs.get('control_group')
        treatment_group = kwargs.get('treatment_group')
        return difference_in_differences(metric_id, pre_period, post_period, control_group, treatment_group)
    else:
        raise ValueError(f"Unknown computation type: {computation_type}")