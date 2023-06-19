from flask import Flask, render_template, jsonify

main = Flask(__name__)
JOBS = [
  {
    'id': 1,
    'title': 'Data analyst',
    'location': 'Benaluru,India',
    'salary': 'Rs.10000'
  },
  {
    'id': 2,
    'title': 'Data scrien',
    'location': 'Deihl,India',
    'salary': 'Rs.150000'
  },
  {
    'id': 3,
    'title': 'App website',
    'location': 'Remote',
    'salary': 'Rs.20000'
  },
]


@main.route('/')
def hello_world():
  return render_template('home.html', job=JOBS, company_name='kha')


@main.route("/api/jobs")
def job_list():
  return jsonify(JOBS)


if __name__ == "__main__":
  main.run(host="0.0.0.0", debug=True)
