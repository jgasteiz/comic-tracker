import { Component, Input, Output, EventEmitter } from '@angular/core';

@Component({
    selector: 'spinner',
    styleUrls: ['spinner.component.scss'],
    template: `
        <div class="spinner" *ngIf="loading">
            <div class="dot1"></div>
            <div class="dot2"></div>
        </div>
    `
})
export class SpinnerComponent {
    @Input() loading: boolean;

    constructor() {}
}
