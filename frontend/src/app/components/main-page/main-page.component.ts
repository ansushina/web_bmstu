import {Component, OnInit} from '@angular/core';

@Component({
  selector: 'app-main-page',
  templateUrl: './main-page.component.html',
  styleUrls: ['./main-page.component.scss']
})
export class MainPageComponent implements OnInit {

  constructor() {
    console.log('MAIN PAGE конструктор');
  }

  ngOnInit(): void {
    console.log('MAIN PAGE');
  }

}
