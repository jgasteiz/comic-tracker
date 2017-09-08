from datetime import datetime, date, timedelta

from django import forms

from dashboard.utils import get_closest_wednesday_date


class FetchComicsForm(forms.Form):
    date = forms.ChoiceField(choices=[], widget=forms.RadioSelect)

    def __init__(self, *args, **kwargs):
        super(FetchComicsForm, self).__init__(*args, **kwargs)

        # Add links for fetching comics from the last 10 weeks
        date_choices = []

        closest_wednesday = get_closest_wednesday_date()
        date_choices.append((closest_wednesday, 'Fetch comics from {}'.format(closest_wednesday)))

        # Add the next few Wednesdays after the closest one.
        next_wednesday = closest_wednesday
        for i in range(0, 20):
            next_wednesday = next_wednesday + timedelta(days=7)
            date_choices.insert(0, (next_wednesday, 'Fetch comics from {}'.format(next_wednesday)))

        # Add the previous 9 Wednesdays before the last one.
        previous_wednesday = closest_wednesday
        for i in range(0, 5):
            previous_wednesday = previous_wednesday - timedelta(days=7)
            date_choices.append((previous_wednesday, 'Fetch comics from {}'.format(previous_wednesday)))

        self.fields['date'].choices = date_choices
