import {Genre} from './genre-dto.model';
import {Actor} from './actor-dto.model';
import {Country} from './country-dto.model';

export interface Film{
  id?: number;
  year?: number;
  title?: string;
  description?: string;
  rating?: number;
  genres?: Genre[];
  actors?: Actor[];
  countries?: Country[];
  image?: string;
  created?: string;
}
