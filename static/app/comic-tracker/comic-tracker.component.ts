import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { ComicTrackerService } from './comic-tracker.service';
import { User } from './models/user.interface';

@Component({
    selector: 'comic-tracker',
    providers: [ComicTrackerService],
    template: `
        <nav class="navbar navbar-expand-md navbar-dark bg-dark mb-4">
            <a class="navbar-brand" routerLink="/weekly-releases">Comic Tracker</a>
            <button class="navbar-toggler"
                    type="button"
                    data-toggle="collapse"
                    data-target="#navbarCollapse"
                    aria-controls="navbarCollapse"
                    aria-expanded="false"
                    aria-label="Toggle navigation"
            >
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarCollapse">
                <ul class="navbar-nav mr-auto">
                    <li class="nav-item">
                        <a class="nav-link" routerLink="/weekly-releases">Weekly Releases</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" routerLink="/my-tracked-comics">My Tracked Comics</a>
                    </li>
                </ul>
                <ul class="navbar-nav">
                    <li *ngIf="user" class="nav-item">
                        <a class="nav-link">{{ user.username }}</a>
                    </li>
                </ul>
            </div>
        </nav>
        <div class="container">
            <div class="app">
                <router-outlet></router-outlet>
            </div>
        </div>
    `
})
export class ComicTrackerComponent implements OnInit {
    user: User;

    constructor(private comicTrackerService: ComicTrackerService) {}

    ngOnInit() {
        this.comicTrackerService
            .getUser()
            .subscribe(user => this.user = user);
    }
}
