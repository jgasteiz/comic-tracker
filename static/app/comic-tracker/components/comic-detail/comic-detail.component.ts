import { Component, Input, Output, EventEmitter } from '@angular/core';

import { Comic } from '../../models/comic.interface';
import { User } from '../../models/user.interface';

@Component({
    selector: 'comic-detail',
    styleUrls: ['comic-detail.component.scss'],
    template: `
        <div class="comic-detail">
            <div class="comic-detail__image">
                <img [src]="detail.cover_url">
            </div>
            <div class="comic-detail__info">
                <h2>{{ detail.title }}</h2>
                <p>{{ detail.publisher }}, {{ detail.release_date }}, {{ detail.price }}</p>
                <p>{{ detail.description }}</p>
                <a target="_blank" [href]="detail.external_url">Read more on LCG</a>
                <div class="comic-detail__tracking">
                    <button
                        class="btn btn-sm"
                        [ngClass]="{'btn-danger': detail.is_tracked, 'btn-primary': !detail.is_tracked}"
                        (click)="track(!detail.is_tracked)"
                    >
                        <span *ngIf="!detail.is_tracked">Track</span>
                        <span *ngIf="detail.is_tracked">Untrack</span>
                    </button>
                </div>
            </div>
        </div>
    `
})
export class ComicDetailComponent {
    @Input() detail: Comic;
    @Input() tracked: boolean;

    @Output() onTracked = new EventEmitter<any>();

    constructor() {}

    track(isTracked: boolean) {
        this.onTracked.emit({
            comicId: this.detail.external_id,
            tracked: isTracked
        });
    }
}
