import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './components/app.component';
import { MainPageComponent } from './components/main-page/main-page.component';
import {AppRoutingModule} from './app-routing/app-routing.module';
import { NavbarComponent } from './components/navbar/navbar.component';
import { FilmLittleCardComponent } from './components/main-page/film-little-card/film-little-card.component';
import { FilmCarouselComponent } from './components/main-page/film-carousel/film-carousel.component';
import { FilmPageComponent } from './components/film-page/film-page.component';
import { FilmComponent } from './components/film-page/film/film.component';
import { CommentComponent } from './components/film-page/comment/comment.component';
import { CommentInputComponent } from './components/film-page/comment-input/comment-input.component';
import { SearchPageComponent } from './components/search-page/search-page.component';
import { FilmCardComponent } from './components/search-page/film-card/film-card.component';
import { FiltersComponent } from './components/search-page/filters/filters.component';
import { SettingsPageComponent } from './components/settings-page/settings-page.component';
import { LoginPageComponent } from './components/login-page/login-page.component';
import { RegistarationPageComponent } from './components/registaration-page/registaration-page.component';
import {HttpClientModule} from '@angular/common/http';
import {FilmService} from './services/film.service';
import {FormsModule, ReactiveFormsModule} from "@angular/forms";
import {MatSelectModule} from "@angular/material/select";
import {BrowserAnimationsModule} from "@angular/platform-browser/animations";
import { AttributeListComponent } from './components/common/attribute-list/attribute-list.component';

@NgModule({
  declarations: [
    AppComponent,
    MainPageComponent,
    NavbarComponent,
    FilmLittleCardComponent,
    FilmCarouselComponent,
    FilmPageComponent,
    FilmComponent,
    CommentComponent,
    CommentInputComponent,
    SearchPageComponent,
    FilmCardComponent,
    FiltersComponent,
    SettingsPageComponent,
    LoginPageComponent,
    RegistarationPageComponent,
    AttributeListComponent
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    HttpClientModule,
    AppRoutingModule,
    FormsModule,
    MatSelectModule,
    ReactiveFormsModule,

  ],
  providers: [FilmService],
  bootstrap: [AppComponent]
})
export class AppModule { }
