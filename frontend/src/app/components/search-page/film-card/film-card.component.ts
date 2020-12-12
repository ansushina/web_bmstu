import {Component, Input, OnInit} from '@angular/core';
import {Film} from '../../../models/dto/film-dto.model';


const FilmMock =
  {
    id: 1,
    year: 2008,
    title: 'Семь жизней',
    description: 'Инженер Бен отправляется в необычное путешествие. В ходе своей поездки он встречает семерых незнакомцев, включая смертельно больную Эмили, которая называет себя девушкой с подбитыми крыльями. Бен неожиданно влюбляется в нее, что сильно усложняет его первоначальный план. Сможет ли он разгадать послание судьбы?',
    rating: 0,
    genres: [
      {
        name: 'мелодрама',
        id: 2
      },
      {
        name: 'драма',
        id: 1
      }
    ],
    actors: [
      {
        first_name: 'Барри',
        last_name: 'Пеппер',
        id: 103
      },
      {
        first_name: 'Розарио',
        last_name: 'Доусон',
        id: 259
      },
      {

        first_name: 'Эльпидия',
        last_name: 'Каррильо',
        id: 339
      },
      {
        first_name: 'Тим',
        last_name: 'Келлехер',
        id: 813
      },
      {
        first_name: 'Уилл',
        last_name: 'Смит',
        id: 1528
      },
      {
        first_name: 'Вуди',
        last_name: 'Харрельсон',
        id: 1549
      },
      {
        first_name: 'Билл',
        last_name: 'Смитрович',
        id: 1609
      },
      {
        first_name: 'Робин',
        last_name: 'Ли',
        id: 1642
      },
      {
        first_name: 'Майкл',
        last_name: 'Или',
        id: 1789
      },
      {
        first_name: 'Джо',
        last_name: 'Нуньес',
        id: 1802
      }
    ],
    countries: [
      {
        name: 'США',
        id: 1
      }
    ],
    image: '/films/2020/11/16/new',
    created: '2020-11-16T23:03:12.724388+03:00'
  };


@Component({
  selector: 'app-film-card',
  templateUrl: './film-card.component.html',
  styleUrls: ['./film-card.component.scss']
})
export class FilmCardComponent implements OnInit {

  @Input() public film: Film;

  constructor() { }

  ngOnInit(): void {
    this.film = FilmMock;
  }

}
