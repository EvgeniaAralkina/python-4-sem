# Python

<h3>Games statistic</h3>
Проанализировать <a href="https://github.com/Newbilius/Old-Games_DOS_Game_Gauntlet/blob/master/GAMES.csv">базу данных</a> старых компьютерных игр.

С помощью графиков ответить на следующие вопросы:

  1. Какие годы были самыми популярными с точки зрения выхода игр?
  2. Какие жанры были популярны в различные периоды времени?

<h3>students_statistic</h3>
Проанализировать данные, полученные от <a href="https://github.com/true-grue/kispython/tree/main/pract3"> почтового бота</a>

С помощью графиков ответить на следующие вопросы:

  1. Как по времени суток распределяется активность студентов?
  2. Как по дням недели распределяется активность студентов?
  3. В каких группах было отправлено больше всего сообщений?
  4. В каких группах было получено больше всего правильных решений?
  5. Какие задачи оказались самыми легкими, самыми сложными?
  6. Какие распространенные ошибки совершали студенты?

<h3>Schelling's_segregation</h3>

Реализовать модель сегрегации Шеллинга в Matplotlib. На двумерной сетке находятся агенты двух групп. На каждой клетке может находиться не более 1 агента. Агент "счастлив", если, как минимум, заданный процент ближайших соседей относится к его группе. В противном случае агент переезжает на иное, свободное место.

Ввести следующие параметры: размер популяции, размеры сетки, процентное соотношение агентов двух групп, пороговое значение "толерантности", количество шагов моделирования.
<ul>
<li>Реализовать отображение агентов в виде квадратов двух цветов на целочисленной сетке.</li>
<li>Случайно разместить агентов, учитывая запрет на совпадение координат.</li>
<li>Реализовать функцию distance на основе метрики манхэттенского расстояния.</li>
<li>Реализовать функцию is_happy.</li>
<li>Изобразить график исходного расположения агентов и график расположения спустя N шагов моделирования.</li>
<li>Изобразить график изменения состояния "настроения" агентов.</li>
<li>(повышенной сложности) Реализовать анимацию шагов моделирования.</li>
</ul>

<h3>fustMul_fustPow</h3>

Реализуйте функцию fast_mul в соответствии с алгоритмом двоичного умножения в столбик.
Реализуйте аналогичную функцию fast_pow для возведения в степень.
