import { NgModule } from '@angular/core';
import {RouterModule, Routes} from '@angular/router';
import {MainPageComponent} from '../components/main-page/main-page.component';
import {SettingsPageComponent} from '../components/settings-page/settings-page.component';
import {LoginPageComponent} from '../components/login-page/login-page.component';
import {RegistarationPageComponent} from '../components/registaration-page/registaration-page.component';
import {FilmPageComponent} from '../components/film-page/film-page.component';
import {SearchPageComponent} from '../components/search-page/search-page.component';

const routes: Routes = [
  { path: 'home', component: MainPageComponent },
  { path: 'settings', component: SettingsPageComponent},
  { path: 'login', component: LoginPageComponent},
  { path: 'registration', component: RegistarationPageComponent},
  { path: 'film/:id', component: FilmPageComponent},
  { path: 'search', component: SearchPageComponent},
  { path: '**', redirectTo: 'home' },
];


@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
