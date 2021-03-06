from django.urls import path
from apps.task.views import  DeleteView, AddTaskView, AddTaskSelfView, UpdateTaskState, \
    TaskCommentsView, UserTaskView, UpdateTask, \
    TaskFilterStatusCreatedViewSet, TaskFilterStatusInprocessViewSet, TaskFilterStatusFinishedViewSet, \
    TaskSearchViewSet, UserTaskCreatedView, AllRedisTasksView, RedisInitView
from rest_framework.routers import DefaultRouter
from apps.time_tracker.views import TimeTrackerLogsView, TopDurationTimeView

from apps.time_tracker.views import TimeTrackerStartView, TimeTrackerAddLogView, TimeTrackerStop

router = DefaultRouter()
# router.register(r'', TaskViewSet.as_view(), base_name='al')
router.register(r'created', TaskFilterStatusCreatedViewSet, base_name='task_list_status')
router.register(r'open', TaskFilterStatusInprocessViewSet, base_name='task_list_status')
router.register(r'closed', TaskFilterStatusFinishedViewSet, base_name='task_list_status')
router.register(r'search', TaskSearchViewSet, base_name='all_tasks')
urlpatterns = router.urls

urlpatterns += [
    path('all/', AllRedisTasksView.as_view(), name='task_list'),

    path('delete_task/<int:pk>/', DeleteView.as_view(), name='delete_task'),
    path('create/', AddTaskView.as_view(), name='task_create'),
    path('create_self/', AddTaskSelfView.as_view(), name='task_create_self'),
    path('task_update/', UpdateTask.as_view(), name="update_task"),

    path('<int:pk>/start/', TimeTrackerStartView.as_view(), name='start_time'),
    path('<int:pk>/add_log/', TimeTrackerAddLogView.as_view(), name='add_log'),
    path('<int:pk>/stop/', TimeTrackerStop.as_view(), name='tasks_all_details_stop_time'),
    path('<int:pk>/logs/', TimeTrackerLogsView.as_view(), name='time_logs'),
    path('top_duration/', TopDurationTimeView.as_view(), name="top_20"),

    path('<int:pk>/', TaskCommentsView.as_view(), name='tasks_all_details'),
    path('my_created/', UserTaskView.as_view(), name='task_user_assigned'),
    path('my_assigned/', UserTaskCreatedView.as_view(), name='task_user_created'),
    path('update_status/', UpdateTaskState.as_view(), name="update_status"),

    path('redis_init/', RedisInitView.as_view(), name='redis_init'),
]

for i in range(1, 4):
    del urlpatterns[1]
