class Loader:

    def __init__(self, current_dir=None):
        
        # Prepare attributes
        self._data_dir = current_dir + '\\dailydialog\\data\\'

        # Load dialoges
        # One dialogue: many utterances
        self._dialogue_dict = self._load_dialogues()
        print(self._dialogue_dict)

        # Load act annotations
        # One dialogue: many act

        # Perform mapping

    def _load_dialogues(self) -> dict:
        
        utterances_dict = {}
        with open(f'{self._curr_dir}\dialogues_text.txt', encoding='utf-8') as f:

            for index, line in enumerate(f.readlines()):

                # Replace the un-processed character
                # and remove newline character
                line = line.replace('’',"'").rstrip('\n')
                utterances_dict[index] = line.split('__eou__')

        return utterances_dict

    def _load_act_labels(self) -> list:
        pass

    def _map_utter_act(self) -> None:
        pass