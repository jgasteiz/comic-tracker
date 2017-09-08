import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';

import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';

import { Observable } from 'rxjs/Rx';

import { Comic } from './models/comic.interface';

import * as moment from 'moment';

@Injectable()
export class ComicTrackerService {
    static getCookie(name) {
        let cookieValue: string;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i];
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    static getDateFormat(): string {
        return 'YYYY-MM-DD';
    }

    static getClosestWednesday(date: moment.Moment): moment.Moment {
        const wednesdayWeekday = 3;
        const previousWednesdayOffset = (date.weekday() - wednesdayWeekday) % 7;
        const nextWednesdayOffset = (wednesdayWeekday - date.weekday()) % 7;
        if (previousWednesdayOffset < nextWednesdayOffset) {
            return date.subtract(previousWednesdayOffset, 'days');
        } else {
            return date.add(nextWednesdayOffset, 'days');
        }
    }

    static getMomentDateFromString(date: string): moment.Moment {
        let momentDate = moment(date, ComicTrackerService.getDateFormat());
        if (!momentDate.isValid()) {
            momentDate = moment();
        }
        return momentDate;
    }

    static getStringFromMomentDate(momentDate: moment.Moment): string {
        return momentDate.format(ComicTrackerService.getDateFormat());
    }

    static substractDaysFromMomentDate(momentDate: moment.Moment, numDays): moment.Moment {
        return momentDate.clone().subtract(7, 'days');
    }

    static addDaysToMomentDate(momentDate: moment.Moment, numDays): moment.Moment {
        return momentDate.clone().add(7, 'days');
    }

    constructor(private http: HttpClient) {}

    getUser(): any {
        return this.http.get('/api/users/');
    }

    getReleases(date: string): Observable<Comic[]> {
        return this.http
            .get(`/api/new-releases/?date=${date}`);
    }

    getUserTrackedComics(date: string): Observable<Comic[]> {
        return this.http
            .get(`/api/tracked-comics/?date=${date}`);
    }

    trackComic(comicId: number, tracked: boolean): Observable<Comic> {
        const body = {
            tracked: tracked,
        };
        return this.http.put(`/api/comics/${comicId}/`, body);
    }
}
