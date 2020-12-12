import {Component, Input, OnInit} from '@angular/core';
import {Film} from "../../../models/dto/film-dto.model";

@Component({
  selector: 'app-film-carousel',
  templateUrl: './film-carousel.component.html',
  styleUrls: ['./film-carousel.component.scss']
})
export class FilmCarouselComponent implements OnInit {
  @Input() films: Film[];
  constructor() { }

  ngOnInit(): void {
  }

}
