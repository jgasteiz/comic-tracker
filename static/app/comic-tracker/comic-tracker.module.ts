import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { RouterModule, Routes } from '@angular/router';

// Module component
import { ComicTrackerComponent } from './comic-tracker.component';

// Containers
import { ComicReleasesComponent } from './containers/comic-releases/comic-releases.component';

// Components
import { ComicDetailComponent } from './components/comic-detail/comic-detail.component';

const appRoutes: Routes = [
    {
        path: 'my-tracked-comics/:date',
        component: ComicReleasesComponent
    },
    {
        path: 'my-tracked-comics',
        component: ComicReleasesComponent
    },
    {
        path: 'weekly-releases/:date',
        component: ComicReleasesComponent
    },
    {
        path: 'weekly-releases',
        component: ComicReleasesComponent
    },
    {
        path: '',
        redirectTo: '/weekly-releases',
        pathMatch: 'full',
    }
];

@NgModule({
    declarations: [
        ComicTrackerComponent,
        ComicReleasesComponent,
        ComicDetailComponent,
    ],
    imports: [
        CommonModule,
        FormsModule,
        RouterModule.forRoot(
            appRoutes,
            {
                enableTracing: true,
                useHash: true,
            }),
    ],
    exports: [
        ComicTrackerComponent,
    ]
})
export class ComicTrackerModule {}
