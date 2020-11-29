input="$(dirname "$0")/../envfile"
while IFS= read -r line; do
    export "$line"
done <"$input"


# docker_file=$(dirname "$0")/../Dockerfile

docker build -t $docker_tag -f $(dirname "$0")/../Dockerfile .


docker run -ti $docker_tag bash