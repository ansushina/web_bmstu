import {Component, OnInit} from '@angular/core';
import {Film} from '../../models/dto/film-dto.model';
import {Comment} from '../../models/dto/comment-dto.model';
import {ActivatedRoute} from '@angular/router';
import {FilmService} from '../../services/film.service';


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

const CommentsMock =
  [
    {
      text: 'jklhkgjkl',
      author: {
        username: 'vasya111',
        email: 'vasya',
        avatar: 'avatars/2020/11/17/Снимок_экрана_от_2020-06-09_10-57-44.png',
        created: '2020-11-17T15:31:18.951221+03:00',
        id: 1
      },
      film: 1,
      created: '2020-11-17T15:31:53.307976+03:00',
      id: 1
    },
    {
      text: 'jklhkgjkl121212',
      author: {
        username: 'vasya111',
        email: 'vasya',
        avatar: 'avatars/2020/11/17/Снимок_экрана_от_2020-06-09_10-57-44.png',
        created: '2020-11-17T15:31:18.951221+03:00',
        id: 1
      },
      film: 1,
      created: '2020-11-17T15:32:15.425231+03:00',
      id: 2
    },
    {
      text: 'jklhkgjkl121212',
      author: {
        username: 'vasya111',
        email: 'vasya',
        avatar: 'avatars/2020/11/17/Снимок_экрана_от_2020-06-09_10-57-44.png',
        created: '2020-11-17T15:31:18.951221+03:00',
        id: 1
      },
      film: 1,
      created: '2020-11-17T15:33:33.454453+03:00',
      id: 3
    },
    {
      text: 'jklhkgjkl121212',
      author: {
        username: 'vasya111',
        email: 'vasya',
        avatar: 'avatars/2020/11/17/Снимок_экрана_от_2020-06-09_10-57-44.png',
        created: '2020-11-17T15:31:18.951221+03:00',
        id: 1
      },
      film: 1,
      created: '2020-11-17T15:33:36.785024+03:00',
      id: 4
    },
    {
      text: 'jklhkgjkl121212',
      author: {
        username: 'vasya111',
        email: 'vasya',
        avatar: 'avatars/2020/11/17/Снимок_экрана_от_2020-06-09_10-57-44.png',
        created: '2020-11-17T15:31:18.951221+03:00',
        id: 1
      },
      film: 1,
      created: '2020-11-17T15:33:39.220958+03:00',
      id: 5
    },
    {
      text: 'jklhkgjkl121212',
      author: {
        username: 'vasya111',
        email: 'vasya',
        avatar: 'avatars/2020/11/17/Снимок_экрана_от_2020-06-09_10-57-44.png',
        created: '2020-11-17T15:31:18.951221+03:00',
        id: 1
      },
      film: 1,
      created: '2020-11-17T15:35:14.060027+03:00',
      id: 6
    },
    {
      text: 'jklhkgjkl121212',
      author: {
        username: 'vasya111',
        email: 'vasya',
        avatar: 'avatars/2020/11/17/Снимок_экрана_от_2020-06-09_10-57-44.png',
        created: '2020-11-17T15:31:18.951221+03:00',
        id: 1
      },
      film: 1,
      created: '2020-11-17T15:36:02.509055+03:00',
      id: 7
    },
    {
      text: 'jklhkgjkl121212',
      author: {
        username: 'vasya111',
        email: 'vasya',
        avatar: 'avatars/2020/11/17/Снимок_экрана_от_2020-06-09_10-57-44.png',
        created: '2020-11-17T15:31:18.951221+03:00',
        id: 1
      },
      film: 1,
      created: '2020-11-17T15:36:04.836686+03:00',
      id: 8
    },
    {
      text: 'jklhkgjkl121212',
      author: {
        username: 'vasya111',
        email: 'vasya',
        avatar: 'avatars/2020/11/17/Снимок_экрана_от_2020-06-09_10-57-44.png',
        created: '2020-11-17T15:31:18.951221+03:00',
        id: 1
      },
      film: 1,
      created: '2020-11-17T15:36:05.687940+03:00',
      id: 9
    },
    {
      text: 'jklhkgjkl121212',
      author: {
        username: 'vasya111',
        email: 'vasya',
        avatar: 'avatars/2020/11/17/Снимок_экрана_от_2020-06-09_10-57-44.png',
        created: '2020-11-17T15:31:18.951221+03:00',
        id: 1
      },
      film: 1,
      created: '2020-11-17T15:37:13.357462+03:00',
      id: 10
    }
  ];


@Component({
  selector: 'app-film-page',
  templateUrl: './film-page.component.html',
  styleUrls: ['./film-page.component.scss']
})
export class FilmPageComponent implements OnInit {

  public film: Film;

  public comments: Comment[];

  private id: number;

  constructor(private route: ActivatedRoute, private filmService: FilmService) {
    this.id = +this.route.snapshot.paramMap.get('id');
  }

  onclick(): void {
    fetch('http://localhost/api/v1/films/1/', {
      mode: 'cors',
    })
      .then(res => res.json())
      .then(
        (res) => {
          this.film = res;
        },
        (err) => {
          console.log(err);
        }
      );
  }

  ngOnInit(): void {
    // this.film = FilmMock;
    // this.comments = CommentsMock;
    this.filmService.getFilm(this.id).subscribe(
      film => this.film = film,
      err => console.log('Error: ', err)
    );

    this.filmService.getComments(this.id).subscribe(
      comments => this.comments = comments,
      error => console.log(error),
    );
  }
}
