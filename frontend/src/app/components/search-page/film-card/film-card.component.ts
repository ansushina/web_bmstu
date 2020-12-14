import {Component, Input, OnInit} from '@angular/core';
import {Film} from '../../../models/dto/film-dto.model';


@Component({
  selector: 'app-film-card',
  templateUrl: './film-card.component.html',
  styleUrls: ['./film-card.component.scss']
})
export class FilmCardComponent implements OnInit {

  @Input() public film: Film;

  constructor() {
  }

  ngOnInit(): void {
  }

}
