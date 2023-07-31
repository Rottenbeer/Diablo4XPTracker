import logging

from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

from .configreader import ConfigReader


class NoCallbackRegisteredException(Exception):
    pass


class ScreenshotWatcher:
    def __init__(self, config: ConfigReader) -> None:
        self._config = config
        path = self._config.screenshot_path

        self._patterns = ["*.jpg"]
        self._ignore_patterns = None
        self._ignore_directories = False
        self._case_sensitive = True
        self._my_event_handler = PatternMatchingEventHandler(
            self._patterns,
            self._ignore_patterns,
            self._ignore_directories,
            self._case_sensitive,
        )
        self._my_event_handler.on_created = self.on_created  # type: ignore
        self._my_event_handler.on_deleted = self.on_deleted  # type: ignore
        self._my_event_handler.on_modified = self.on_modified  # type: ignore
        self._my_event_handler.on_moved = self.on_moved  # type: ignore
        go_recursively = False
        self._my_observer = Observer()
        self._my_observer.schedule(
            self._my_event_handler, path, recursive=go_recursively
        )
        self.on_created_callback = None
        self.on_deleted_callback = None
        self.on_modified_callback = None
        self.on_moved_callback = None

    def start_watcher(self) -> None:
        self._my_observer.start()

    def stop_watcher(self) -> None:
        self._my_observer.stop()
        self._my_observer.join()

    def register_on_created_callback(self, callback) -> None:
        self.on_created_callback = callback

    def register_on_deleted_callback(self, callback) -> None:
        self.on_deleted_callback = callback

    def register_on_modified_callback(self, callback) -> None:
        self.on_modified_callback = callback

    def register_on_moved_callback(self, callback) -> None:
        self.on_moved_callback = callback

    def on_created(self, event) -> None:
        logging.debug(f"{event.src_path} has been created!")
        if not self.on_created_callback:
            return
        self.on_created_callback(event.src_path)

    def on_deleted(self, event) -> None:
        logging.debug(f"Deleted {event.src_path}!")
        if not self.on_deleted_callback:
            return
        self.on_deleted_callback(event.src_path)

    def on_modified(self, event) -> None:
        logging.debug(f"{event.src_path} has been modified")
        if not self.on_modified_callback:
            return
        self.on_modified_callback(event.src_path)

    def on_moved(self, event) -> None:
        logging.debug(f"Moved {event.src_path} to {event.dest_path}")
        if not self.on_moved_callback:
            return
        self.on_moved_callback(event.src_path, event.dest_path)
