drop table if exists participant;
create table participant (
	id serial,
	full_name text,
	gender text,
	birth date,
	ages int,
	city text,
	job text,
	institution text,
	email text,
	handphone text,
	programs text,
	price int,
	duration text,
	starting_date date,
	ending_date date
);

insert into participant (full_name, gender, birth, ages, city, job, institution, email, handphone, programs, price, duration, starting_date, ending_date)
values
  ('Jerome Polin', 'male', '2008-01-01', 15, 'Surabaya', 'Student', 'SMAN 5 Surabaya', 'jeromepolin@gmail.com', '6283812345876', 'General English', 2000000, '2 months', '2023-10-01', '2023-11-30'),
  ('Maudy Ayunda', 'female', '2007-12-31', 16, 'Jombang', 'Student', 'SMAN 2 Jombang', 'maudyayunda@gmail.com', '6283896329864', 'Intensive IELTS', 3000000, '3 months', '2023-09-01', '2023-11-30'),
  ('Tiara Andini', 'female', '2006-11-30', 17, 'Bekasi', 'Student', 'SMAN 1 Bekasi', 'tiaraandini@gmail.com', '6283886234109', 'TOEFL Preparation', 2500000, '2 months', '2023-10-01', '2023-11-30'),
  ('Jefri Nichol', 'male', '2005-10-31', 18, 'Banyuwangi', 'Barista', 'Point Coffee', 'jefrinichol@gmail.com', '628385316457', 'Business English', 3500000, '3 months', '2023-09-01', '2023-11-30'),
  ('Iqbaal Ramadhan', 'male', '2004-09-30', 19, 'Pasuruan', 'College Student', 'Unair', 'iqbaalramadhan@gmail.com', '6283894583190', 'Conversational English', 2000000, '2 months', '2023-10-01', '2023-11-30'),
  ('Syifa Hadju', 'female', '2003-08-31', 20, 'Gresik', 'College Student', 'Unika Atma Jaya', 'syifahadju@gmail.com', '6283820432211', 'General English', 3000000, '3 months', '2023-09-01', '2023-11-30'),
  ('Ziva Magnolya', 'female', '2002-07-31', 21, 'Kediri', 'College Student', 'Upn Veteran', 'zivamagnolya@gmail.com', '6283874820274', 'Intensive IELTS', 2500000, '2 months', '2023-10-01', '2023-11-30'),
  ('Refal Hadi', 'male', '2001-06-30', 22, 'Sidoarjo', 'College Student', 'ITS', 'refalhadi@gmail.com', '6283873628496', 'TOEFL Preparation', 3500000, '3 months', '2023-09-01', '2023-11-30'),
  ('Angga Yunanda', 'male', '2000-05-31', 23, 'Malang', 'College Student', 'UI', 'anggayunanda@gmail.com', '6283872947145', 'Business English', 2000000, '2 months', '2023-09-01', '2023-10-30')
;

select * from participant;