SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

CREATE TABLE `Conference` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `Division` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `conference` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `Standings` (
  `id` int(11) NOT NULL,
  `team` int(11) NOT NULL,
  `year` year(4) NOT NULL,
  `win` smallint(6) NOT NULL,
  `loss` smallint(6) NOT NULL,
  `pct` float NOT NULL,
  `gb` float NOT NULL,
  `conf_win` smallint(6) NOT NULL,
  `conf_loss` smallint(6) NOT NULL,
  `div_win` smallint(6) NOT NULL,
  `div_loss` smallint(6) NOT NULL,
  `home_win` smallint(6) NOT NULL,
  `home_loss` smallint(6) NOT NULL,
  `road_win` smallint(6) NOT NULL,
  `road_loss` smallint(6) NOT NULL,
  `l10_win` tinyint(4) NOT NULL,
  `l10_loss` tinyint(4) NOT NULL,
  `streak` smallint(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `Team` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `division` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


ALTER TABLE `Conference`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `conference_name_uniq_idx` (`name`);

ALTER TABLE `Division`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`id`),
  ADD KEY `division_conference_fk` (`conference`);

ALTER TABLE `Standings`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `standings_team_fk` (`team`,`year`) USING BTREE;

ALTER TABLE `Team`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `team_name_idx` (`name`),
  ADD KEY `team_division_fk` (`division`);


ALTER TABLE `Conference`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=257;
ALTER TABLE `Division`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=196;
ALTER TABLE `Standings`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=871;
ALTER TABLE `Team`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1055;

ALTER TABLE `Division`
  ADD CONSTRAINT `division_conference_fk` FOREIGN KEY (`conference`) REFERENCES `Conference` (`id`);

ALTER TABLE `Standings`
  ADD CONSTRAINT `standings_team_fk` FOREIGN KEY (`team`) REFERENCES `Team` (`id`);

ALTER TABLE `Team`
  ADD CONSTRAINT `team_division_fk` FOREIGN KEY (`division`) REFERENCES `Division` (`id`);

