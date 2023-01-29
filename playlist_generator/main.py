import click

from api.spotify import Spotify


@click.command()
@click.argument("song")
def main(song):
    spotify = Spotify()
    spotify.connect()
    songs = spotify.search(song)
    for song in songs:
        sample_track_id = songs.tracks.items[0].item_id
        features = spotify.get_tracks_audio_features(sample_track_id)
        print(features)

if __name__ == "__main__":
    main()