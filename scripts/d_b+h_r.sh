input="$(dirname "$0")/../envfile"
while IFS= read -r line; do
    export "$line"
done <"$input"

docker build -t $docker_tag -f $(dirname "$0")/../Dockerfile .

heroku container:push web -a $heroku_app

heroku container:release web -a $heroku_app
