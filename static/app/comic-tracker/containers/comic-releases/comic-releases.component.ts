import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';

// Models
import { Comic } from '../../models/comic.interface';

// Services
import { ComicTrackerService } from '../../comic-tracker.service';

@Component({
    providers: [ComicTrackerService],
    styleUrls: ['comic-releases.component.scss'],
    selector: 'comic-releases',
    template: `
        <div class="row">
            <div class="col col-sm-8">
                <h1 *ngIf="mode === 'all-comics'">Weekly releases</h1>
                <h1 *ngIf="mode === 'tracked-comics'">My Tracked Comics</h1>
            </div>
            <div class="col col-sm-4 text-right">
                <strong>Week: {{ currentWednesdayDate }}</strong>
                <div class="btn-group">
                    <a class="btn btn-primary"
                       routerLink="/weekly-releases/{{ previousWednesdayDate }}"
                       *ngIf="mode === 'all-comics'"
                    >Previous week</a>
                    <a class="btn btn-primary"
                       routerLink="/my-tracked-comics/{{ previousWednesdayDate }}"
                       *ngIf="mode === 'tracked-comics'"
                    >Previous week</a>
                    <a class="btn btn-primary"
                       routerLink="/weekly-releases/{{ nextWednesdayDate }}"
                       *ngIf="mode === 'all-comics'"
                    >Next week</a>
                    <a class="btn btn-primary"
                       routerLink="/my-tracked-comics/{{ nextWednesdayDate }}"
                       *ngIf="mode === 'tracked-comics'"
                    >Next week</a>
                </div>
            </div>
        </div>

        <hr>

        <h2 *ngIf="!loadingComics && comicList.length == 0">There are no comics for this date.</h2>

        <ul class="comic-list">
            <li *ngFor="let comic of comicList;" class="comic-list__item">
                <comic-detail
                    [detail]="comic"
                    (onTracked)="onTracked($event)"
                ></comic-detail>
            </li>
        </ul>
        <spinner [loading]="loadingComics"></spinner>
    `
})
export class ComicReleasesComponent implements OnInit {
    comicList: Comic[];
    loadingComics: boolean;
    currentWednesdayDate: string;
    previousWednesdayDate: string;
    nextWednesdayDate: string;

    // Determines in which `mode` the component is:
    // - tracked comics (for a given week)
    // or
    // - all comics for a given week
    mode: string;

    constructor(
        private route: ActivatedRoute,
        private router: Router,
        private comicTrackerService: ComicTrackerService,
    ) {
        this.comicList = [];
        this.loadingComics = false;
    }

    ngOnInit() {
        this.route.params.subscribe(params => {
            this.parseRouteAndFetchComics();
        });
    }

    parseRouteAndFetchComics() {
        this.comicList = [];
        this.loadingComics = true;

        // Get a valid moment.Moment object from the url.
        const momentDate = ComicTrackerService.getMomentDateFromString(this.route.snapshot.paramMap.get('date'));

        // Get the closest Wednesday.
        const currentWednesdayMomentDate = ComicTrackerService.getClosestWednesday(momentDate);
        this.currentWednesdayDate = ComicTrackerService.getStringFromMomentDate(currentWednesdayMomentDate);

        // Get the previous Wednesday from the closest wednesday.
        this.previousWednesdayDate = ComicTrackerService.getStringFromMomentDate(
            ComicTrackerService.substractDaysFromMomentDate(currentWednesdayMomentDate, 7)
        );
        // Get the next Wednesday from the closest wednesday.
        this.nextWednesdayDate = ComicTrackerService.getStringFromMomentDate(
            ComicTrackerService.addDaysToMomentDate(currentWednesdayMomentDate, 7)
        );

        // If we're in `my tracked comics`, get the user's tracked comics
        // from the closest Wednesday.
        // Otherwise get the closest Wednesday releases.
        if (this.router.url.indexOf('/my-tracked-comics') >= 0) {
            this.mode = 'tracked-comics';
            this.comicTrackerService
                .getUserTrackedComics(this.currentWednesdayDate, comicList => {
                    this.comicList = comicList;
                    this.loadingComics = false;
                });
        } else {
            this.mode = 'all-comics';
            this.comicTrackerService
                .getReleases(this.currentWednesdayDate, comicList => {
                    this.comicList = comicList;
                    this.loadingComics = false;
                });
        }
    }

    onTracked(trackedData: any) {
        this.comicTrackerService
            .trackComic(trackedData['comicId'], trackedData['tracked'])
            .subscribe(updatedComic => {
                const comicToUpdate = this.comicList.find(comic => comic.pk === updatedComic.pk);
                comicToUpdate.tracked_by = updatedComic.tracked_by;
                comicToUpdate.is_tracked = updatedComic.is_tracked;
            });
    }
}
