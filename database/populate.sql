INSERT INTO arch (name) VALUES
        ('desktop'),
        ('ipad');

INSERT INTO distribution(name) VALUES
        ('cnx'),
        ('openstax');

INSERT INTO suite(name) VALUES
        ('latex'),
        ('princexml');

INSERT INTO format(name) VALUES
        ('completezip'),
        ('pdf'),
        ('offlinezip'),
        ('epub');

INSERT INTO suitearches(suite_id, arch_id, master_weight) VALUES (
        (SELECT id FROM suite WHERE name='latex'),
        (SELECT id FROM arch WHERE name='desktop'),
        0
);

INSERT INTO suitearches(suite_id, arch_id,master_weight) VALUES (
        (SELECT id FROM suite WHERE name='princexml'),
        (SELECT id FROM arch WHERE name='desktop'),
        1
);

INSERT INTO suitearches(suite_id, arch_id,master_weight) VALUES (
        (SELECT id FROM suite WHERE name='latex'),
        (SELECT id FROM arch WHERE name='ipad'),
        0
);

INSERT INTO suitearches(suite_id, arch_id,master_weight) VALUES (
        (SELECT id FROM suite WHERE name='princexml'),
        (SELECT id FROM arch WHERE name='ipad'),
        1
);

INSERT INTO status(name) VALUES
        ('Waiting'),
        ('Blocked'),
        ('Cancelled'),
        ('Building'),
        ('Failed'),
--        ('Uploaded'),
        ('Done');
