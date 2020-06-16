from flask import Blueprint, jsonify, request, render_template #, flash, redirect

from web_apps.models import Tweet, User, db, parse_records

tweet_routes = Blueprint("tweet_routes", __name__)

@tweet_routes.route("/tweets.json")
def list_users():
    # tweets = [
    #     {"id": 1, "title": "Tweet 1"},
    #     {"id": 2, "title": "Tweet 2"},
    #     {"id": 3, "title": "Tweet 3"},
    # ]
    tweet_records = Tweet.query.all()
    print(book_records)
    tweets = parse_records(tweet_records)
    return jsonify(tweets)

@tweet_routes.route("/tweets")
def list_tweets_for_humans():
    # tweets = [
    #     {"id": 1, "title": "Tweet 1"},
    #     {"id": 2, "title": "Tweet 2"},
    #     {"id": 3, "title": "Tweet 3"},
    # ]
    tweet_records = Tweet.query.all()
    print(tweet_records)
    tweet = parse_records(tweet_records) # optionally
    return render_template("tweets.html", message="Here's some tweets", tweets=tweets)

@tweet_routes.route("/tweets/new")
def new_user():
    return render_template("new_tweet.html")

@tweet_routes.route("/tweets/create", methods=["POST"])
def create_user():
    print("FORM DATA:", dict(request.form))
   
    new_tweet = Tweet(title=request.form["tweet_title"], user_id=request.form["user_name"])
    db.session.add(new_tweet)
    db.session.commit()

    return jsonify({
        "message": "TWEET CREATED OK",
        "tweet": dict(request.form)
    })
    #flash(f"Book '{new_book.title}' created successfully!", "success")
    #return redirect(f"/books")