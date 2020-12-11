import {Component, Input, OnInit} from '@angular/core';
import {Film} from '../../../models/dto/film-dto.model';

@Component({
  selector: 'app-film',
  templateUrl: './film.component.html',
  styleUrls: ['./film.component.scss']
})
export class FilmComponent implements OnInit {

  @Input() public film: Film;
  constructor() { }

  ngOnInit(): void {
  }

}
