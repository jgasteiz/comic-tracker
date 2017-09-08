import { CommonModule } from '@angular/common';
import { HttpClientModule, HttpClientXsrfModule } from '@angular/common/http';
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { ComicTrackerModule } from './comic-tracker/comic-tracker.module';

@NgModule({
    declarations: [
        AppComponent,
    ],
    imports: [
        // Angular modules
        BrowserModule,
        HttpClientModule,
        HttpClientXsrfModule.withOptions({
            cookieName: 'csrftoken',
            headerName: 'HTTP_X_CSRFTOKEN',
        }),
        CommonModule,
        // Custom modules
        ComicTrackerModule,
    ],
    bootstrap: [AppComponent]
})
export class AppModule {}
