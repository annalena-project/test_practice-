from flask import Flask, abort, render_template, redirect, request, url_for
from Extra.task_manager import TaskManager

app = Flask(__name__)

task_manager = TaskManager()


@app.route("/")
def home():
    return "Weather Tracker Homepage!"


@app.route("/observations", methods=["GET", "POST"])
def observations():

    if request.method == "POST":

        title = request.form.get("title")
        description = request.form.get("description", "")

        new_task = task_manager.create({
            "title": title,
            "description": description
        })

        return redirect(url_for("observation", observation_id=new_task["id"]))

    else:

        tasks = task_manager.read()
        return render_template("tasks/index.html", tasks=tasks)


@app.route("/observations/<int:observation_id>")
def observation(observation_id):

    task = task_manager.read(observation_id)

    if not task:
        abort(404)

    return render_template("tasks/show.html", task=task)


@app.route("/observations/<int:observation_id>/edit", methods=["GET", "POST"])
def edit_observation(observation_id):

    task = task_manager.read(observation_id)

    if not task:
        abort(404)

    if request.method == "POST":

        title = request.form.get("title")
        description = request.form.get("description", "")

        task_manager.update(observation_id, {
            "title": title,
            "description": description
        })

        return redirect(url_for("observation", observation_id=observation_id))

    else:

        return render_template("tasks/edit.html", task=task)


@app.route("/observations/<int:observation_id>/delete", methods=["POST"])
def delete_observation(observation_id):

    task = task_manager.read(observation_id)

    if not task:
        abort(404)

    task_manager.delete(observation_id)

    return redirect(url_for("observations"))


if __name__ == "__main__":
    app.run(debug=True)