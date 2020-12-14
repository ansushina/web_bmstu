import {Component, Input, OnInit} from '@angular/core';
import {Film} from '../../../models/dto/film-dto.model';

@Component({
  selector: 'app-film-little-card',
  templateUrl: './film-little-card.component.html',
  styleUrls: ['./film-little-card.component.scss']
})
export class FilmLittleCardComponent implements OnInit {

  @Input() film: Film;

  constructor() {
  }

  ngOnInit(): void {
  }

}
