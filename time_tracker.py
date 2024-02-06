from flask import Flask, jsonify, request
print("hello")

@bp.route('/timesheet', methods=['POST'])
def add_timesheet():
    timesheets = []
    total_hours = 0
    timesheet_data = request.json.get('timesheet_data')

    if not timesheet_data:
        return jsonify({"error": "No timesheet data provided"})        

    for data in timesheet_data:
        project_id = data.get('project_id')
        qpmtask_id = data.get('qpmtask_id')
        task_id = data.get('task_id')
        subtask_id = data.get('subtask_id')
        task_status = data.get('task_status')
        hours = int(data.get('hours'))
        description = data.get('description')

        if hours < 4 or hours > 12:
            return jsonify({"error": "Invalid hours input. Hours should be between 4 and 12."})

        total_hours += hours

        if total_hours > 12:
            return jsonify({"error": "Total hours exceed the limit of 12 hours."})

        if hours > 0:
            timesheet = Timesheet(project_id=project_id, qpmtask_id=qpmtask_id, task_id=task_id,
                                  subtask_id=subtask_id, task_status=task_status, hours=hours, description=description)
            timesheets.append(timesheet)

    db.session.add_all(timesheets)
    db.session.commit()

    return jsonify({"message": "Timesheet added successfully"})
    # project_id = request.form.get('project_id')
    # qpmtask_id = request.form.get('qpmtask_id')
    # task_id = request.form.get('task_id')
    # subtask_id = request.form.get('subtask_id')
    # task_status = request.form.get('task_status')
    # hours = int(request.form.get('hours'))
    # description = request.form.get('description')
    
    # if hours < 4 or hours > 12:
    #     return jsonify({"error": "Invalid hours input. Hours should be between 4 and 12."})

    # timesheet = Timesheet(project_id=project_id, qpmtask_id=qpmtask_id, task_id=task_id, subtask_id=subtask_id,
    #                       task_status=task_status, hours=hours, description=description)
    # db.session.add(timesheet)
    # db.session.commit()

    # return jsonify({"message": "Timesheet added successfully"})